"""Ruleset validation must reject authoring errors before static deployment."""
import copy
import hashlib
import json
import subprocess
from pathlib import Path
import pytest
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import validate_rulesets as rulesets

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT/'data/rulesets/reference-2026-11-10/r1/manifest.json'
STUDY = ROOT/'data/rulesets/shaman-investment-study/r1/manifest.json'


def catalog():
    return {(m['id'], m['revision']): (p, m) for p in (ROOT/'data/rulesets').glob('*/r*/manifest.json') for m in [rulesets.read(p)]}


def test_all_shipped_revisions_pass():
    for path, m in catalog().values():
        assert rulesets.validate_revision(ROOT, path, m, catalog()) == []


@pytest.mark.parametrize('mutation, message', [
    (lambda m: m.update(revision=2), 'directory'),
    (lambda m: m.update(unknownRule=True), 'manifest'),
    (lambda m: m['baseline'].update(revision=99), 'missing baseline'),
    (lambda m: m['changes']['shaman'].pop('totemic-relay'), 'intent'),
    (lambda m: m['changes']['shaman'].update(stale='unused'), 'intent'),
    (lambda m: m['hashes'].update({'../escape':'0'*64}), 'missing/unsafe'),
    (lambda m: m['hashes'].update({next(iter(m['hashes'])):'0'*64}), 'content changed'),
    (lambda m: m['hashes'].clear(), 'manifest'),
])
def test_invalid_manifest_fails(mutation, message):
    m = copy.deepcopy(rulesets.read(STUDY))
    mutation(m)
    assert any(message in e for e in rulesets.validate_revision(ROOT, STUDY, m, catalog()))


@pytest.mark.parametrize('mutation, message', [
    (lambda c: c['trees'][0]['talents'][0].update(excludes=['x']), 'Additional properties'),
    (lambda c: c['trees'][0]['talents'][0].update(maxRank=10), 'greater than'),
    (lambda c: c['trees'][0]['talents'].append(copy.deepcopy(c['trees'][0]['talents'][0])), 'already used'),
    (lambda c: c['trees'][0]['talents'][0].update(requires=[{'talent':'missing','rank':1}]), 'does not exist'),
    (lambda c: c['trees'][0]['talents'][0].update(row=99), 'row'),
    (lambda c: c['trees'][0]['talents'][0].update(ranks=[]), 'non-empty'),
])
def test_invalid_effective_dataset_fails(mutation, message):
    c = rulesets.read(STUDY.parent/'classes/shaman.json')
    mutation(c)
    assert any(message.lower() in e.lower() for e in rulesets.validate_class(ROOT, STUDY.parent/'classes/shaman.json', c, True))


def test_snapshot_and_encoding_are_captured_from_source():
    m=rulesets.read(BASE)
    for class_id in m['classes']:
        original=subprocess.check_output(['git','show',f'{m["sourceCommit"]}:data/talents/{class_id}.json'],cwd=ROOT)
        assert original == (BASE.parent/'classes'/f'{class_id}.json').read_bytes()
    before=json.loads(subprocess.check_output(['git','show',f'{m["sourceCommit"]}:data/encoding/v1.json'],cwd=ROOT))
    after=rulesets.read(BASE.parent/'encoding/v1.json')
    assert before['classes']==after['classes']
    assert after['frozen'] is True


def test_new_baseline_does_not_rebase_an_existing_experiment(tmp_path):
    # The same static catalog may contain a later baseline; the pin remains authoritative.
    entries=catalog()
    newer=copy.deepcopy(entries[('reference-2026-11-10',1)][1])
    newer.update(id='reference-next',revision=2)
    entries[('reference-next',2)]=(tmp_path/'manifest.json',newer)
    assert rulesets.validate_revision(ROOT,STUDY,rulesets.read(STUDY),entries)==[]
    assert rulesets.read(STUDY)['baseline']=={'id':'reference-2026-11-10','revision':1}


def test_retained_revisions_cannot_be_rewritten_or_deleted(tmp_path):
    subprocess.run(['git','init','-q',str(tmp_path)],check=True)
    folder=tmp_path/'data/rulesets/reference/r1';folder.mkdir(parents=True)
    asset=tmp_path/'icon.jpg';asset.write_bytes(b'original')
    (folder/'manifest.json').write_text(json.dumps({'hashes':{'icon.jpg':hashlib.sha256(asset.read_bytes()).hexdigest()}}))
    subprocess.run(['git','add','.'],cwd=tmp_path,check=True)
    subprocess.run(['git','-c','user.name=Test','-c','user.email=test@example.invalid','commit','-qm','fixture'],cwd=tmp_path,check=True)
    assert rulesets.retained_changes(tmp_path,'HEAD')==[]
    asset.write_bytes(b'changed')
    assert any('asset changed' in e for e in rulesets.retained_changes(tmp_path,'HEAD'))
    (folder/'manifest.json').unlink()
    assert any('revision changed' in e for e in rulesets.retained_changes(tmp_path,'HEAD'))


def test_authoring_cli_creates_new_revision_and_refuses_to_reseal_tracked_data(tmp_path, monkeypatch):
    import shutil
    import ruleset as authoring
    subprocess.run(['git','init','-q',str(tmp_path)],check=True)
    paths=set(rulesets.read(STUDY)['hashes']) | {
        str(STUDY.relative_to(ROOT)), str(BASE.relative_to(ROOT)),
        str((BASE.parent/'classes/shaman.json').relative_to(ROOT)),
        'data/schema/class.schema.json','data/schema/experimental-class.schema.json','data/schema/ruleset.schema.json',
    }
    for name in paths:
        target=tmp_path/name
        target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(ROOT/name,target)
    monkeypatch.setattr(authoring,'ROOT',tmp_path)
    monkeypatch.setattr(sys,'argv',['ruleset.py','create','--from-id','shaman-investment-study','--id','study-next','--revision','1','--name','Next study','--class','shaman'])
    authoring.main()
    target=tmp_path/'data/rulesets/study-next/r1'
    created=rulesets.read(target/'manifest.json')
    assert created['baseline']==rulesets.read(STUDY)['baseline']
    assert created['changes']==rulesets.read(STUDY)['changes']
    assert rulesets.read(target/'classes/shaman.json')==rulesets.read(STUDY.parent/'classes/shaman.json')
    assert set(created['hashes']) != set(rulesets.read(STUDY)['hashes'])
    subprocess.run(['git','add','.'],cwd=tmp_path,check=True)
    with pytest.raises(ValueError,match='already tracked'):
        authoring.seal(target)


def test_experimental_schema_only_relaxes_unobserved_manual_design_ranks():
    reference=rulesets.read(ROOT/'data/schema/class.schema.json')
    experimental=rulesets.read(ROOT/'data/schema/experimental-class.schema.json')
    for key in ['$id','title']:
        experimental[key]=reference[key]
    experimental['$defs']['talent']['properties']['ranksObserved']['minItems']=1
    special=experimental['$defs']['talent']['allOf'].pop()
    assert special['then']['properties']['ranksObserved']['maxItems']==0
    assert special['then']['properties']['ranksSource']['const']=='manual'
    assert experimental==reference
