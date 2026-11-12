"""Create and seal repository-authored experiments. Published revisions are never edited."""
import argparse
import hashlib
import json
import shutil
import subprocess
from pathlib import Path
import validate_rulesets as validation

ROOT = Path(__file__).resolve().parents[1]


def write(path, value):
    path.write_text(json.dumps(value, indent=2) + '\n')


def untracked(folder):
    tracked = subprocess.check_output(['git', 'ls-files', '--', str(folder.relative_to(ROOT))], cwd=ROOT, text=True)
    if tracked:
        raise ValueError('Revision is already tracked. Create a new revision; seal before git add.')


def seal(folder):
    untracked(folder)
    path = folder/'manifest.json'
    m = validation.read(path)
    if m['kind'] != 'experiment':
        raise ValueError('This command seals experiments only.')
    classes = {p.stem: validation.read(p) for p in (folder/'classes').glob('*.json')}
    if set(classes) != set(m['classes']):
        raise ValueError('Class files must match manifest.classes.')
    versions = {c['dataVersion'] for c in classes.values()}
    if len(versions) != 1:
        raise ValueError('Use one encoding version for a new experiment revision.')
    order = {'version':versions.pop(), 'frozen':True, 'classes':{}}
    assets = set()
    for id, c in classes.items():
        pages = {p['id']: i for i, p in enumerate(c['pages'])}
        trees = sorted(c['trees'], key=lambda t:(pages[t['page']], t['order']))
        order['classes'][id] = {'trees':[t['id'] for t in trees], 'order':{
            t['id']:[x['id'] for x in sorted(t['talents'],key=lambda x:(x['row'],x['col']))] for t in trees}}
        for tree in c['trees']:
            if tree.get('source',{}).get('crop'):
                assets.add(tree['source']['crop'])
            for t in tree['talents']:
                assets.add(t.get('iconCrop',f'web/public/icons/{t["icon"]}.jpg'))
                if t['source'].get('crop'):
                    assets.add(t['source']['crop'])
    enc = folder/'encoding'
    enc.mkdir(exist_ok=True)
    for old in enc.glob('v*.json'):
        old.unlink()  # untracked revision only; never the source revision
    write(enc/f'v{order["version"]}.json',order)
    files = [p for p in folder.rglob('*.json') if p != path] + [ROOT/a for a in sorted(assets)]
    for p in files:
        if not p.resolve().is_relative_to(ROOT) or not p.is_file():
            raise ValueError(f'Missing or unsafe retained file: {p.name}')
    m['hashes'] = {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(files)}
    write(path,m)
    catalog={}
    for mp in (ROOT/'data/rulesets').glob('*/r*/manifest.json'):
        manifest=validation.read(mp)
        catalog[(manifest['id'],manifest['revision'])]=(mp,manifest)
    errors=validation.validate_revision(ROOT,path,m,catalog)
    if errors:
        raise ValueError('\n'.join(errors))
    print(f'Sealed {m["id"]} revision {m["revision"]}; review and commit these files together.')


def main():
    p=argparse.ArgumentParser(description=__doc__)
    commands=p.add_subparsers(dest='command',required=True)
    create=commands.add_parser('create')
    create.add_argument('--from-id',required=True)
    create.add_argument('--from-revision',type=int,default=1)
    create.add_argument('--id',required=True)
    create.add_argument('--revision',type=int,required=True)
    create.add_argument('--name',required=True)
    create.add_argument('--class',dest='class_id',required=True)
    refresh=commands.add_parser('seal')
    refresh.add_argument('--id',required=True)
    refresh.add_argument('--revision',type=int,required=True)
    args=p.parse_args()
    import re
    if not re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*',args.id) or args.revision<1:
        p.error('Use a slug ID and positive integer revision.')
    folder=ROOT/'data/rulesets'/args.id/f'r{args.revision}'
    try:
        if args.command=='create':
            if not re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*',args.from_id) or args.from_revision<1:
                raise ValueError('Invalid source identity.')
            source=ROOT/'data/rulesets'/args.from_id/f'r{args.from_revision}'
            original=validation.read(source/'manifest.json')
            if args.class_id not in original['classes']:
                raise ValueError('Source revision does not support this class.')
            if folder.exists():
                raise ValueError('Target revision already exists; use a new revision.')
            (folder/'classes').mkdir(parents=True)
            shutil.copy2(source/'classes'/f'{args.class_id}.json',folder/'classes'/f'{args.class_id}.json')
            baseline=original.get('baseline',{'id':original['id'],'revision':original['revision']})
            m={'schemaVersion':1,'kind':'experiment','id':args.id,'revision':args.revision,'name':args.name,
               'classes':[args.class_id],'baseline':baseline,'intent':'Describe this experiment and its opportunity costs.',
               'changes':{args.class_id:original.get('changes',{}).get(args.class_id,{})},'hashes':{}}
            write(folder/'manifest.json',m)
        seal(folder)
    except (ValueError, OSError, KeyError) as e:
        p.exit(1,f'{e}\n')


if __name__=='__main__':
    main()
