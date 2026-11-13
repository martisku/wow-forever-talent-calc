"""Validate retained rulesets without reference export/encoding assumptions."""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from jsonschema import Draft202012Validator
import validate as reference

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BASELINE = ('reference-2026-11-10', 1)


def read(path):
    return json.loads(path.read_text())


def talents(doc):
    return {t['id']: (tree['id'], t) for tree in doc['trees'] for t in tree['talents']}


def semantic(t):
    return {k: v for k, v in t.items() if k not in {'source', 'ranksSource', 'ranksObserved', 'ranksPrior', 'ranksNote'}}


def changed_ids(before, after):
    a, b = talents(before), talents(after)
    return {id for id in a.keys() | b.keys() if id not in a or id not in b
            or a[id][0] != b[id][0] or semantic(a[id][1]) != semantic(b[id][1])}


def validate_class(root, path, doc, experimental=False):
    schema = read(root / ('data/schema/experimental-class.schema.json' if experimental else 'data/schema/class.schema.json'))
    ctx = reference.Ctx(path, root, argparse.Namespace(no_files=False), schema, None)
    if not reference.rule_1_schema(ctx, doc):
        return [f.message for f in ctx.result.findings]
    for rule in (reference.rule_2_ids, reference.rule_3_rules, reference.rule_4_pages_trees,
                 reference.rule_5_talents, reference.rule_6_ranks, reference.rule_7_rank_sources,
                 reference.rule_8_requires, reference.rule_9_files, reference.rule_10_source,
                 reference.rule_13_row_gating):
        rule(ctx, doc)
    return [f'{f.path}: {f.message}' for f in ctx.result.findings if f.level == 'ERROR']


def validate_revision(root, path, m, catalog):
    errors = []
    schema_errors = list(Draft202012Validator(read(root/'data/schema/ruleset.schema.json')).iter_errors(m))
    if schema_errors:
        return [f'manifest: {e.message}' for e in schema_errors]
    folder = path.parent
    if folder.name != f'r{m["revision"]}' or folder.parent.name != m['id']:
        errors.append('manifest identity does not match directory')
    actual = {p.stem for p in (folder/'classes').glob('*.json')}
    if actual != set(m['classes']):
        errors.append('class files do not match manifest classes')
    required = {p.relative_to(root).as_posix() for p in folder.rglob('*.json') if p != path}
    for file, digest in m['hashes'].items():
        target = (root/file).resolve()
        if not target.is_relative_to(root.resolve()) or not target.is_file():
            errors.append(f'missing/unsafe retained file: {file}')
        elif hashlib.sha256(target.read_bytes()).hexdigest() != digest:
            errors.append(f'retained content changed: {file}')
    if not required <= m['hashes'].keys():
        errors.append('hashes do not cover all revision files')
    if m.get('source'):
        source = m['source']
        raw = folder/'source/talents.js'
        if not raw.is_file() or hashlib.sha256(raw.read_bytes()).hexdigest() != source['dataSha256']:
            errors.append('publisher source hash does not match retained data')
        discovery = folder/'source/discovery.json'
        if not discovery.is_file() or any(read(discovery).get(k) != v for k, v in source.items()):
            errors.append('publisher provenance does not match discovery evidence')
    baseline = None
    if m['kind'] == 'experiment':
        pin = m['baseline']
        baseline = catalog.get((pin['id'], pin['revision']))
        if not baseline or baseline[1]['kind'] != 'baseline':
            return errors + ['missing baseline pin']
        if set(m['changes']) != set(m['classes']):
            errors.append('change intent must cover exactly the supported classes')
    orders = {}
    for ep in (folder/'encoding').glob('v*.json'):
        e = read(ep)
        if e.get('frozen') is not True:
            errors.append(f'{ep.name}: published encoding must be frozen')
        if e['version'] in orders:
            errors.append('duplicate encoding version')
        orders[e['version']] = e
    for class_id in sorted(actual):
        cp = folder/'classes'/f'{class_id}.json'
        c = read(cp)
        class_errors = validate_class(root, cp, c, m['kind'] == 'experiment')
        errors.extend(f'{class_id}: {e}' for e in class_errors)
        if class_errors:
            continue
        if m.get('source'):
            for tree in c['trees']:
                for talent in tree['talents']:
                    src = talent['source']
                    expected = {'kind':'wowhead','url':m['source']['dataUrl'], **{key:m['source'][key] for key in ('version','dataRevision','retrievedAt')}}
                    if any(src.get(key) != value for key,value in expected.items()):
                        errors.append(f'{class_id}: publisher provenance mismatch')
        if c['rules']['maxPoints'] != 51:
            errors.append(f'{class_id}: v1 requires a 51-point budget')
        e = orders.get(c['dataVersion'], {}).get('classes', {}).get(class_id)
        if not e or len(e['trees']) != len(set(e['trees'])) or set(e['trees']) != {t['id'] for t in c['trees']}:
            errors.append(f'{class_id}: missing or invalid encoding trees')
        else:
            if set(e['order']) != set(e['trees']):
                errors.append(f'{class_id}: invalid encoding order keys')
            for tree in c['trees']:
                ids = e['order'].get(tree['id'], [])
                if len(ids) != len(set(ids)) or set(ids) != {t['id'] for t in tree['talents']}:
                    errors.append(f'{class_id}/{tree["id"]}: encoding coverage mismatch')
        for tree in c['trees']:
            if tree.get('source',{}).get('crop') and tree['source']['crop'] not in m['hashes']:
                errors.append(f'{class_id}: tree asset not retained')
            for t in tree['talents']:
                assets = [t.get('iconCrop'), t['source'].get('crop')]
                if not t.get('iconCrop'):
                    assets.append(f'web/public/icons/{t["icon"]}.jpg')
                for asset in filter(None, assets):
                    if asset not in m['hashes']:
                        errors.append(f'{class_id}: asset not retained: {asset}')
        if baseline:
            bp, bm = baseline
            if class_id not in bm['classes']:
                errors.append(f'{class_id}: unsupported by baseline')
                continue
            b = read(bp.parent/'classes'/f'{class_id}.json')
            if c['rules'] != b['rules'] or c['pages'] != b['pages']:
                errors.append(f'{class_id}: rule/page changes are outside v1')
            def tree_meta(doc):
                return [{k:v for k,v in t.items() if k != 'talents'} for t in doc['trees']]
            if tree_meta(c) != tree_meta(b):
                errors.append(f'{class_id}: tree metadata changes are outside v1')
            changed = changed_ids(b, c)
            if changed != m['changes'].get(class_id, {}).keys():
                errors.append(f'{class_id}: missing or stale change intent')
            for id in changed:
                entry = talents(c).get(id)
                if entry and entry[1]['source']['kind'] != 'manual':
                    errors.append(f'{class_id}/{id}: custom design must have manual provenance')
    return errors


def retained_changes(root, base):
    """Published revisions and shared assets are append-only relative to the PR base."""
    errors = []
    names = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', base, 'data/rulesets'], cwd=root, text=True).splitlines()
    for name in names:
        old = subprocess.check_output(['git', 'show', f'{base}:{name}'], cwd=root)
        if not (root/name).is_file() or (root/name).read_bytes() != old:
            errors.append(f'published revision changed or removed: {name}')
        if name.endswith('/manifest.json'):
            for file, digest in json.loads(old)['hashes'].items():
                if not (root/file).is_file() or hashlib.sha256((root/file).read_bytes()).hexdigest() != digest:
                    errors.append(f'published asset changed or removed: {file}')
    return errors


def validate_current_reference(root, catalog):
    path = root/'data/current-reference.json'
    if not path.is_file():
        return ['current reference pointer is missing']
    current = read(path)
    if (not {'ruleset','revision'} <= set(current) or not set(current) <= {'ruleset','revision','source'} or not isinstance(current['ruleset'], str)
            or type(current['revision']) is not int or current['revision'] < 1):
        return ['invalid current reference pointer']
    entry = catalog.get((current['ruleset'],current['revision']))
    if not entry or entry[1]['kind'] != 'baseline':
        return ['current reference must name a retained baseline']
    source = entry[1].get('source')
    preview = {key:source[key] for key in ('version','retrievedAt')} if source else None
    if current.get('source') != preview:
        return ['current reference source label does not match the retained baseline']
    classes = {p.stem for p in (root/'data/talents').glob('*.json')}
    if not classes <= set(entry[1]['classes']):
        return ['current reference does not cover all reference classes']
    return []


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', help='Git base ref for append-only verification')
    args = parser.parse_args()
    paths = sorted((ROOT/'data/rulesets').glob('*/r*/manifest.json'))
    catalog, errors = {}, []
    for path in paths:
        m = read(path)
        key = (m.get('id'), m.get('revision'))
        if key in catalog:
            errors.append(f'duplicate identity: {key}')
        catalog[key] = (path, m)
    if DEFAULT_BASELINE not in catalog:
        errors.append('legacy baseline is missing')
    for path, m in catalog.values():
        errors.extend(f'{path.relative_to(ROOT)}: {e}' for e in validate_revision(ROOT, path, m, catalog))
    errors.extend(validate_current_reference(ROOT, catalog))
    if args.base:
        errors.extend(retained_changes(ROOT, args.base))
    for error in errors:
        print(f'ERROR {error}')
    print(f'{len(paths)} ruleset revision(s): {len(errors)} error(s)')
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())
