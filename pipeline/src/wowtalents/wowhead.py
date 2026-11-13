"""Read the public data used by Wowhead's Forever calculator, without executing JS.

This is a website adapter, not an official supported API. Unknown environments,
missing ranks or unsupported rules are errors, never invitations to use Classic.
"""
from __future__ import annotations

import hashlib
import json
import re
import time
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, parse_qs
from typing import Callable

from wowtalents import fsio
from wowtalents.db2 import now_rfc3339

PAGE_URL = 'https://www.wowhead.com/forever/talent-calc/shaman'
DATA_KEY = 'wow.talentCalcClassic.classicplus.data'
USER_AGENT = 'wow-forever-talent-calc/1 (+https://github.com/martisku/wow-forever-talent-calc)'
# Explicit supported tree mapping/order. A new or reassigned tree must be reviewed.
TREES = {
    'druid': [('283', 'Balance'), ('281', 'FeralCombat'), ('282', 'Restoration')],
    'hunter': [('361', 'BeastMastery'), ('363', 'Marksmanship'), ('362', 'Survival')],
    'mage': [('81', 'Arcane'), ('41', 'Fire'), ('61', 'Frost')],
    'paladin': [('382', 'Holy'), ('383', 'Protection'), ('381', 'Combat')],
    'priest': [('201', 'Discipline'), ('202', 'Holy'), ('203', 'Shadow')],
    'rogue': [('182', 'Assassination'), ('181', 'Combat'), ('183', 'Subtlety')],
    'shaman': [('261', 'ElementalCombat'), ('263', 'Enhancement'), ('262', 'Restoration')],
    'warlock': [('302', 'Curses'), ('303', 'Summoning'), ('301', 'Destruction')],
    'warrior': [('161', 'Arms'), ('164', 'Fury'), ('163', 'Protection')],
}


def strict_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f'Duplicate source key: {key}')
        result[key] = value
    return result


DECODER = json.JSONDecoder(object_pairs_hook=strict_object)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.meta_parts = []
        self.sources = []
        self.in_meta = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'script':
            self.in_meta = attrs.get('id') == 'data.pageMeta'
            if attrs.get('src'):
                self.sources.append(unescape(attrs['src']))

    def handle_endtag(self, tag):
        if tag == 'script':
            self.in_meta = False

    def handle_data(self, data):
        if self.in_meta:
            self.meta_parts.append(data)


def discover(body: bytes) -> dict:
    p = Page()
    p.feed(body.decode('utf-8'))
    meta = DECODER.decode(''.join(p.meta_parts))
    env = meta['dataEnv']
    if env.get('env') != 16 or env.get('tree') != 16 or env.get('maxLevel') != 60:
        raise ValueError('Expected the level-60 Forever environment (16), not Classic/PTR/another game.')
    version = env['versions']['16']
    revision = str(meta['activeDbChanged']['16'])
    if not re.fullmatch(r'\d+\.\d+\.\d+', version) or not revision.isdigit():
        raise ValueError('Missing or unsupported Forever version/revision.')
    urls = [u for u in p.sources if urlparse(u).netloc == 'nether.wowhead.com'
            and urlparse(u).scheme == 'https' and urlparse(u).path == '/forever/data/talents-classic']
    if len(urls) != 1:
        raise ValueError('Expected exactly one Forever talent data script in the page.')
    query = parse_qs(urlparse(urls[0]).query)
    if set(query) != {'dv','db'} or query.get('db') != [revision] or len(query.get('dv', [])) != 1 or not query['dv'][0].isdigit():
        raise ValueError('Page metadata and talent data revision disagree.')
    return {'provider': 'wowhead', 'pageUrl': PAGE_URL, 'dataUrl': urls[0],
            'version': version, 'dataRevision': revision, 'environment': 16}


def parse_payload(body: bytes) -> dict:
    script = body.decode('utf-8-sig')
    pattern = r'WH\.setPageData\(\s*"' + re.escape(DATA_KEY) + r'"\s*,\s*'
    matches = list(re.finditer(pattern, script))
    if len(matches) != 1:
        raise ValueError('Expected exactly one Forever calculator dataset; refusing fallback data.')
    data, end = DECODER.raw_decode(script, matches[0].end())
    if not re.match(r'\s*\);', script[end:]):
        raise ValueError('Talent data is not a JSON argument followed by a closed setPageData call.')
    if not isinstance(data, dict) or not isinstance(data.get('talents'), dict) or not isinstance(data.get('trees'), dict):
        raise ValueError('Unsupported talent dataset structure.')
    return data


class Text(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)

    def handle_starttag(self, tag, attrs):
        if tag in ('br', 'p', 'div', 'table', 'tr', 'td', 'th'):
            self.parts.append(' ')
        elif tag not in ('span', 'b', 'strong', 'i', 'em', 'a'):
            raise ValueError(f'Unexpected markup in rank text: {tag}')


def plain_text(value):
    if not isinstance(value, str):
        raise ValueError('Rank text must be a string.')
    p = Text()
    p.feed(value)
    result = ' '.join(''.join(p.parts).split())
    if not result or re.search(r'[{}]|\|[cr]', result) or any(t != '$mcrit' for t in re.findall(r'\$[a-zA-Z0-9]+', result)):
        raise ValueError('Empty or unresolved rank text; no estimates will be substituted.')
    return result


def number(value, label, minimum=0, maximum=None):
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum or (maximum is not None and value > maximum):
        raise ValueError(f'Invalid {label}: {value!r}')
    return value


def convert(payload: dict, source: dict) -> dict[str, dict]:
    expected = {id for trees in TREES.values() for id, _ in trees}
    if set(payload['trees']) != expected or set(payload['talents']) != expected:
        raise ValueError('Expected all 27 supported class trees, with no missing or unknown trees.')
    docs = {}
    provenance = {'kind': 'wowhead', 'url': source['dataUrl'], 'version': source['version'],
                  'dataRevision': source['dataRevision'], 'retrievedAt': source['retrievedAt'], 'reviewed': False}
    for cls, mapping in TREES.items():
        trees, seen = [], set()
        for order, (tree_id, tree_name) in enumerate(mapping):
            meta = payload['trees'][tree_id]
            if meta.get('id') != int(tree_id) or meta.get('description') != cls.capitalize() + tree_name:
                raise ValueError(f'Unexpected tree identity: {tree_id}')
            raw = payload['talents'][tree_id]
            if not isinstance(raw, dict) or not raw:
                raise ValueError(f'Empty or invalid tree: {tree_id}')
            names = {str(t['id']): f'wh-{t["id"]}' for t in raw.values()}
            talents, cells = [], set()
            for key, t in raw.items():
                if set(t) != {'id','row','col','icon','name','ranks','definition','descriptions','requires','requiredPoints'}:
                    raise ValueError('Talent source fields changed; review the adapter before importing.')
                id = number(t['id'], 'talent ID', 1)
                if str(id) != key or id in seen:
                    raise ValueError('Duplicate or mismatched talent identity.')
                seen.add(id)
                row = number(t['row'], 'row', 0, 6)
                col = number(t['col'], 'column', 0, 3)
                if (row, col) in cells or number(t.get('requiredPoints'), 'required points') != row * 5:
                    raise ValueError('Duplicate grid cell or unsupported tier gating.')
                cells.add((row, col))
                ranks = t['ranks']
                if not isinstance(ranks, list) or not 1 <= len(ranks) <= 9:
                    raise ValueError('Unsupported rank count.')
                for spell in ranks:
                    number(spell, 'spell ID', 1)
                descriptions = t['descriptions']
                if set(descriptions) != {str(i) for i in range(1, len(ranks) + 1)}:
                    raise ValueError(f'Missing rank descriptions for talent {id}.')
                texts = [plain_text(descriptions[str(i)]) for i in range(1, len(ranks) + 1)]
                if not isinstance(t['icon'], str) or not re.fullmatch(r'[a-z0-9_]+', t['icon']):
                    raise ValueError('Unsupported icon filename.')
                talent = {'id': f'wh-{id}', 'name': plain_text(t['name']), 'row': row, 'col': col,
                          'maxRank': len(ranks), 'icon': t['icon'], 'iconSource': 'wowhead',
                          'description': texts[0], 'ranks': texts, 'ranksObserved': list(range(1, len(ranks) + 1)),
                          'ranksSource': 'observed', 'spellIds': ranks.copy(),
                          'source': {**provenance, 'upstreamTalentId': id}}
                unresolved = sorted(set(re.findall(r'\$[a-zA-Z0-9]+', ' '.join(texts))))
                if unresolved:
                    talent['source']['unresolved'] = unresolved
                    talent['source']['note'] = 'Unresolved publisher formula; retained verbatim without inventing values.'
                reqs = t['requires']
                if not isinstance(reqs, list) or len(reqs) > 3:
                    raise ValueError('Unsupported prerequisites.')
                if reqs:
                    talent['requires'] = []
                    for req in reqs:
                        if set(req) != {'id','qty'}:
                            raise ValueError('Unsupported prerequisite fields.')
                        target = names.get(str(req['id']))
                        if target is None:
                            raise ValueError('Dangling or cross-tree prerequisite.')
                        talent['requires'].append({'talent': target, 'rank': number(req['qty'], 'prerequisite rank', 1, 9)})
                talents.append(talent)
            name = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', tree_name)
            trees.append({'id': name.lower().replace(' ', '-'), 'name': name, 'page': 'primary',
                          'order': order, 'icon': sorted(talents, key=lambda t:(t['row'], t['col']))[0]['icon'],
                          'rows': 7, 'cols': 4, 'talents': sorted(talents, key=lambda t:(t['row'], t['col']))})
        docs[cls] = {'$schema': '../../../../schema/class.schema.json', 'schemaVersion': 1,
                     'class': cls, 'className': cls.capitalize(), 'dataVersion': 1, 'dataSource': 'wowhead',
                     'generatedAt': source['retrievedAt'], 'rules': {'pointsPerRow': 5, 'maxPoints': 51,
                     'firstPointLevel': 10, 'maxLevel': 60, 'rulesSource': 'assumed'},
                     'pages': [{'id': 'primary', 'name': 'Talents'}], 'trees': trees,
                     'notes': ['Published by Wowhead for Forever. May lag hotfixes; not independently verified in game.']}
    return docs


def download(url: str, limit: int = 8_000_000) -> bytes:
    import requests
    with requests.get(url, timeout=(10, 60), stream=True, headers={'User-Agent': USER_AGENT}) as response:
        response.raise_for_status()
        chunks, size = [], 0
        for chunk in response.iter_content(65536):
            size += len(chunk)
            if size > limit:
                raise ValueError('Source response exceeds size limit.')
            chunks.append(chunk)
        return b''.join(chunks)


def verify_bundle(folder: Path) -> dict:
    m = json.loads((folder/'source.json').read_text())
    # Revalidate evidence rather than trusting editable metadata or cached class output.
    body = (folder/'talents.js').read_bytes()
    page = (folder/'page.html').read_bytes()
    discovered = discover(page)
    for key, value in discovered.items():
        if m.get(key) != value:
            raise ValueError('Cached discovery metadata changed.')
    if digest(body) != m['dataSha256'] or digest(page) != m['pageSha256']:
        raise ValueError('Cached source checksum mismatch.')
    parse_payload(body)
    return m


def fetch(cache: Path, get: Callable = download) -> Path:
    page = get(PAGE_URL)
    source = discover(page)
    body = get(source['dataUrl'])
    parse_payload(body)
    folder = cache/f'{source["version"]}-{source["dataRevision"]}-{digest(body)[:12]}'
    if folder.exists():
        cached = verify_bundle(folder)
        if cached['dataSha256'] != digest(body):
            raise ValueError('Cache identity collision.')
        return folder
    source.update(retrievedAt=now_rfc3339(), dataSha256=digest(body), pageSha256=digest(page))
    convert(parse_payload(body), source)  # Fail before keeping an incomplete response.
    folder.mkdir(parents=True)
    try:
        (folder/'page.html').write_bytes(page)
        (folder/'talents.js').write_bytes(body)
        fsio.write_json_atomic(folder/'source.json', source)
    except BaseException:
        import shutil
        shutil.rmtree(folder)
        raise
    return folder


def verify_icon(data: bytes):
    import io
    from PIL import Image
    if len(data) > 200_000:
        raise ValueError('Icon exceeds size limit.')
    try:
        with Image.open(io.BytesIO(data)) as image:
            if image.format != 'JPEG':
                raise ValueError('Icon is not JPEG.')
            image.verify()
    except (OSError, SyntaxError) as e:
        raise ValueError('Invalid JPEG icon.') from e


def cached_icon(bundle: Path, name: str) -> bytes:
    data = (bundle/'icons'/name).read_bytes()
    manifest = json.loads((bundle/'icons.json').read_text())
    entry = manifest.get(name)
    if not entry or entry['sha256'] != digest(data):
        raise ValueError(f'Cached icon checksum mismatch: {name}')
    verify_icon(data)
    return data


def prepare_icons(docs, bundle: Path, root: Path, get: Callable = download, delay=0.5):
    icons = sorted({t['icon'] for c in docs.values() for tree in c['trees'] for t in tree['talents']})
    out = bundle/'icons'
    out.mkdir(exist_ok=True)
    manifest_path = bundle/'icons.json'
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    for icon in icons:
        if (root/f'web/public/icons/{icon}.jpg').is_file():
            continue  # Never replace assets retained by an older revision.
        path = out/f'{icon}.jpg'
        if path.exists():
            cached_icon(bundle, path.name)
            continue
        if delay:
            time.sleep(delay)
        url = f'https://wow.zamimg.com/images/wow/icons/large/{icon}.jpg'
        data = get(url, 200_000)
        verify_icon(data)
        partial = path.with_suffix('.part')
        partial.write_bytes(data)
        partial.replace(path)
        manifest[path.name] = {'url':url,'sha256':digest(data)}
        fsio.write_json_atomic(manifest_path, manifest)
