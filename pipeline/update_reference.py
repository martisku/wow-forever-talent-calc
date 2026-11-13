"""Fetch, prepare and publish a new Wowhead reference snapshot; never rebase experiments."""
from __future__ import annotations
import argparse
import json
import shutil
import subprocess
import tempfile
from pathlib import Path

from wowtalents import db2, fsio, wowhead as W
import validate_rulesets as V

ROOT = Path(__file__).resolve().parents[1]


def prepare(bundle: Path, root: Path = ROOT, *, icons=True) -> dict:
    source = W.verify_bundle(bundle)
    docs = W.convert(W.parse_payload((bundle/'talents.js').read_bytes()), source)
    errors = []
    for cls, doc in docs.items():
        errors.extend(V.validate_class(root, bundle/f'{cls}.json', doc))
    if errors:
        raise ValueError('\n'.join(errors))
    current = json.loads((root/'data/current-reference.json').read_text())
    against = root/'data/rulesets'/current['ruleset']/f'r{current["revision"]}'/'classes'
    diffs = [db2.diff_class(doc, json.loads((against/f'{cls}.json').read_text())) for cls, doc in docs.items()]
    out = bundle/'candidate'
    out.mkdir(exist_ok=True)
    for cls, doc in docs.items():
        fsio.write_json_atomic(out/f'{cls}.json', doc)
    issues = [{'class':c['class'],'talent':t['name'],'tokens':t['source']['unresolved']} for c in docs.values() for tree in c['trees'] for t in tree['talents'] if t['source'].get('unresolved')]
    fsio.write_json_atomic(bundle/'source-issues.json', issues)
    fsio.write_json_atomic(bundle/'comparison.json', {'against':{key:current[key] for key in ('ruleset','revision')}, 'candidateDataHash':source['dataSha256']})
    fsio.write_json_atomic(bundle/'diff.json', diffs)
    fsio.write_text_atomic(bundle/'diff.md', db2.diff_markdown(diffs).replace('Datamined', 'Wowhead').replace('datamined', 'Wowhead').replace('Build `?`', f'Wowhead version {source["version"]}, data revision {source["dataRevision"]}'))
    if icons:
        W.prepare_icons(docs, bundle, root)
    return docs


def publish(bundle: Path, root: Path = ROOT) -> Path:
    # Regenerate from the verified source, not from possibly edited candidate JSON.
    source = W.verify_bundle(bundle)
    id = f'wowhead-forever-{source["version"].replace(".", "-")}-{source["dataRevision"]}-{source["dataSha256"][:12]}'
    parent = root/'data/rulesets'/id
    target = parent/'r1'
    pointer = {'ruleset':id, 'revision':1, 'source':{key:source[key] for key in ('version','retrievedAt')}}
    if target.exists():
        m = V.read(target/'manifest.json')
        if m.get('source',{}).get('dataSha256') != source['dataSha256']:
            raise ValueError('Snapshot identity collision.')
        errors = V.validate_revision(root, target/'manifest.json', m, {})
        if errors:
            raise ValueError('\n'.join(errors))
        pointer['source'] = {key:m['source'][key] for key in ('version','retrievedAt')}
        fsio.write_json_atomic(root/'data/current-reference.json', pointer)
        return target
    docs = prepare(bundle, root, icons=False)
    parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix='.staging-', dir=parent))
    added = []
    installed = False
    try:
        (staging/'classes').mkdir()
        (staging/'encoding').mkdir()
        (staging/'source').mkdir()
        order = {'version':1, 'frozen':True, 'classes':{}}
        assets = set()
        for cls, doc in docs.items():
            fsio.write_json_atomic(staging/'classes'/f'{cls}.json', doc)
            order['classes'][cls] = {'trees':[t['id'] for t in doc['trees']],
                                    'order':{t['id']:[x['id'] for x in t['talents']] for t in doc['trees']}}
            for tree in doc['trees']:
                for t in tree['talents']:
                    asset = root/f'web/public/icons/{t["icon"]}.jpg'
                    assets.add(asset)
                    if not asset.exists():
                        data = W.cached_icon(bundle, asset.name)
                        with asset.open('xb') as f:
                            added.append(asset)
                            f.write(data)
        fsio.write_json_atomic(staging/'encoding/v1.json', order)
        # Keep only public calculator data and discovery evidence, not HTML ad/session markup.
        shutil.copyfile(bundle/'talents.js', staging/'source/talents.js')
        fsio.write_json_atomic(staging/'source/discovery.json', source)
        shutil.copyfile(bundle/'source-issues.json', staging/'source/issues.json')
        shutil.copyfile(bundle/'comparison.json', staging/'source/comparison.json')
        shutil.copyfile(bundle/'diff.json', staging/'source/diff.json')
        shutil.copyfile(bundle/'diff.md', staging/'source/diff.md')
        provenance = {k:source[k] for k in ('provider','pageUrl','dataUrl','version','dataRevision','retrievedAt','dataSha256')}
        m = {'schemaVersion':1,'kind':'baseline','id':id,'revision':1,
             'name':f'Wowhead Forever {source["version"]} ({source["retrievedAt"][:10]})',
             'sourceCommit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip(),
             'classes':sorted(docs), 'intent':'Reference imported from Wowhead’s Forever calculator. May lag hotfixes; not independently verified in game. The shared 51-point budget remains a sandbox rule.',
             'source':provenance, 'hashes':{}}
        for file in staging.rglob('*'):
            if file.is_file():
                m['hashes'][(target/file.relative_to(staging)).relative_to(root).as_posix()] = W.digest(file.read_bytes())
        for asset in assets:
            m['hashes'][asset.relative_to(root).as_posix()] = W.digest(asset.read_bytes())
        m['hashes'] = dict(sorted(m['hashes'].items()))
        fsio.write_json_atomic(staging/'manifest.json', m)
        staging.rename(target)
        installed = True
        errors = V.validate_revision(root, target/'manifest.json', m, {})
        if errors:
            raise ValueError('\n'.join(errors))
        fsio.write_json_atomic(root/'data/current-reference.json', pointer)
        return target
    except BaseException:
        shutil.rmtree(staging, ignore_errors=True)
        if installed:
            shutil.rmtree(target, ignore_errors=True)
        for file in added:
            file.unlink(missing_ok=True)
        if parent.exists() and not any(parent.iterdir()):
            parent.rmdir()
        raise


def main():
    p = argparse.ArgumentParser(description=__doc__)
    commands = p.add_subparsers(dest='command',required=True)
    fetch = commands.add_parser('fetch')
    fetch.add_argument('--cache',type=Path,default=ROOT/'pipeline/work/wowhead-reference')
    for name in ('prepare','publish'):
        command = commands.add_parser(name)
        command.add_argument('--bundle',type=Path,required=True)
    args = p.parse_args()
    try:
        if args.command == 'fetch':
            print(W.fetch(args.cache.resolve()))
        elif args.command == 'prepare':
            docs = prepare(args.bundle.resolve())
            print(f'{len(docs)} classes, {sum(len(t["talents"]) for c in docs.values() for t in c["trees"])} talents')
            print(f'Review {args.bundle}/diff.md before publishing.')
        else:
            print(publish(args.bundle.resolve()))
    except (ValueError, KeyError, TypeError, OSError) as e:
        p.exit(1,f'Reference update failed: {e}\n')


if __name__ == '__main__':
    main()
