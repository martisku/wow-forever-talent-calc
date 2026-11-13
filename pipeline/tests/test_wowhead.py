"""Offline tests for public Forever data discovery, import, integrity and publication."""
import copy
import io
import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from wowtalents import wowhead as W
import update_reference as U
import validate_rulesets as V

REPO = Path(__file__).resolve().parents[2]


def page(env=16, revision='123'):
    meta={'dataEnv':{'env':env,'tree':env,'maxLevel':60,'versions':{'16':'1.60.1'}},'activeDbChanged':{'16':revision}}
    return (f'<script id="data.pageMeta" type="application/json">{json.dumps(meta)}</script>'
            f'<script src="https://nether.wowhead.com/forever/data/talents-classic?dv=34&amp;db={revision}"></script>').encode()


@pytest.fixture
def payload():
    data={'trees':{},'talents':{}}
    for cls, trees in W.TREES.items():
        for id,name in trees:
            data['trees'][id]={'id':int(id),'description':cls.capitalize()+name}
            first=int(id)*10
            data['talents'][id]={str(first):{'id':first,'row':0,'col':0,'icon':'ability_test','name':f'{name} Training',
                'ranks':[111,111],'definition':first+1,'descriptions':{'1':'Increases spells by 2%.','2':'Increases spells by 4%.'},
                'requires':[],'requiredPoints':0}}
    return data


def javascript(data):
    return f'WH.setPageData("{W.DATA_KEY}",{json.dumps(data)});'.encode()


def bundle(tmp_path, payload):
    html=page()
    body=javascript(payload)
    source={**W.discover(html),'retrievedAt':'2026-11-13T12:00:00Z','dataSha256':W.digest(body),'pageSha256':W.digest(html)}
    folder=tmp_path/'bundle';folder.mkdir()
    (folder/'page.html').write_bytes(html)
    (folder/'talents.js').write_bytes(body)
    (folder/'source.json').write_text(json.dumps(source))
    return folder,source


def jpeg():
    out=io.BytesIO();Image.new('RGB',(4,4),'red').save(out,'JPEG');return out.getvalue()


def project(tmp_path,payload):
    root=tmp_path/'repo';root.mkdir()
    schemas=root/'data/schema';schemas.mkdir(parents=True)
    for p in (REPO/'data/schema').glob('*.json'):shutil.copy2(p,schemas/p.name)
    subprocess.run(['git','init','-q',str(root)],check=True)
    subprocess.run(['git','-C',str(root),'-c','user.name=Test','-c','user.email=test@example.invalid','commit','--allow-empty','-qm','fixture'],check=True)
    folder,source=bundle(tmp_path,payload)
    docs=W.convert(payload,source)
    previous=root/'data/rulesets/reference/r1/classes';previous.mkdir(parents=True)
    for cls,doc in docs.items():(previous/f'{cls}.json').write_text(json.dumps(doc))
    (root/'data/current-reference.json').write_text(json.dumps({'ruleset':'reference','revision':1}))
    (root/'web/public/icons').mkdir(parents=True)
    (root/'web/public/icons/ability_test.jpg').write_bytes(jpeg())
    return root,folder


def test_discovery_is_forever_and_cache_revision_is_consistent():
    found=W.discover(page())
    assert found['version']=='1.60.1' and found['dataRevision']=='123'
    assert found['dataUrl'].endswith('dv=34&db=123')
    with pytest.raises(ValueError,match='environment'):W.discover(page(env=4))
    with pytest.raises(ValueError,match='disagree'):W.discover(page().replace(b'db=123',b'db=124'))
    with pytest.raises(ValueError):W.discover(page().replace(b'/forever/data/',b'/classic/data/'))


def test_decode_does_not_execute_script_or_accept_wrong_payload(payload):
    assert W.parse_payload(javascript(payload))==payload
    for data in [javascript(payload).replace(W.DATA_KEY.encode(),b'classic.data'),javascript(payload)*2,
                 f'WH.setPageData("{W.DATA_KEY}",alert(1));'.encode(),f'WH.setPageData("{W.DATA_KEY}",{{"trees":{{}},"trees":{{}},"talents":{{}}}});'.encode()]:
        with pytest.raises(ValueError):W.parse_payload(data)


def test_converter_retains_complete_rank_text_and_stable_upstream_ids(tmp_path,payload):
    folder,source=bundle(tmp_path,payload)
    docs=W.convert(W.parse_payload((folder/'talents.js').read_bytes()),source)
    assert len(docs)==9
    for cls,doc in docs.items():
        assert len(doc['trees'])==3 and doc['rules']['maxPoints']==51
        for tree in doc['trees']:
            t=tree['talents'][0]
            assert t['ranks']==['Increases spells by 2%.','Increases spells by 4%.']
            assert t['spellIds']==[111,111] and t['ranksObserved']==[1,2]
            assert t['id']==f'wh-{t["source"]["upstreamTalentId"]}'
            assert t['source']['kind']=='wowhead'
        assert V.validate_class(REPO,folder/f'{cls}.json',doc)==[]
    changed=copy.deepcopy(payload);changed['talents']['261']['2610']['name']='Renamed training'
    assert W.convert(changed,source)['shaman']['trees'][0]['talents'][0]['id']==docs['shaman']['trees'][0]['talents'][0]['id']


@pytest.mark.parametrize('mutate',[
    lambda d:d['talents'].pop('261'),
    lambda d:d['trees']['261'].update(description='ClassicPlaceholder'),
    lambda d:d['talents']['261']['2610']['descriptions'].pop('2'),
    lambda d:d['talents']['261']['2610'].update(requiredPoints=1),
    lambda d:d['talents']['261']['2610'].update(exclusiveWith=['x']),
    lambda d:d['talents']['261']['2610'].update(requires=[{'id':999,'qty':1}]),
    lambda d:d['talents']['261']['2610'].update(ranks=[True]),
    lambda d:d['talents']['261']['2610'].update(icon='../escape'),
])
def test_source_drift_fails_closed(tmp_path,payload,mutate):
    _,source=bundle(tmp_path,payload);mutate(payload)
    with pytest.raises((ValueError,KeyError)):W.convert(payload,source)


def test_html_text_and_unresolved_publisher_formulas_are_honest(tmp_path,payload):
    assert W.plain_text('A<!--comment--><br><table><tr><td> B &amp; C</td></tr></table>')=='A B & C'
    for text in ['', 'Damage: $unknown', 'Damage: {0}', '<script>bad()</script>']:
        with pytest.raises(ValueError):W.plain_text(text)
    _,source=bundle(tmp_path,payload)
    payload['talents']['261']['2610']['descriptions']['1']='Damage depends on $mcrit.'
    t=W.convert(payload,source)['shaman']['trees'][0]['talents'][0]
    assert t['ranks'][0]=='Damage depends on $mcrit.'
    assert t['source']['unresolved']==['$mcrit'] and 'inventing' in t['source']['note']


def test_fetch_is_cached_and_rejects_corruption(tmp_path,payload):
    calls=[]
    def get(url):
        calls.append(url);return page() if url==W.PAGE_URL else javascript(payload)
    path=W.fetch(tmp_path/'cache',get)
    original=(path/'source.json').read_bytes()
    assert W.fetch(tmp_path/'cache',get)==path
    assert (path/'source.json').read_bytes()==original
    assert len(calls)==4
    (path/'talents.js').write_bytes(b'corrupted')
    with pytest.raises(ValueError,match='checksum'):W.verify_bundle(path)


def test_prepare_publish_and_repeat_leave_old_snapshot_and_experiments_untouched(tmp_path,payload):
    root,folder=project(tmp_path,payload)
    old=(root/'data/rulesets/reference/r1/classes/shaman.json').read_bytes()
    U.prepare(folder,root,icons=False)
    target=U.publish(folder,root)
    pointer=json.loads((root/'data/current-reference.json').read_text())
    assert pointer['ruleset']==target.parent.name
    assert (root/'data/rulesets/reference/r1/classes/shaman.json').read_bytes()==old
    m=V.read(target/'manifest.json')
    assert V.validate_revision(root,target/'manifest.json',m,{})==[]
    frozen={str(p):p.read_bytes() for p in target.rglob('*') if p.is_file()}
    assert U.publish(folder,root)==target
    assert {str(p):p.read_bytes() for p in target.rglob('*') if p.is_file()}==frozen
    (target/'classes/shaman.json').write_text('{}')
    with pytest.raises(ValueError,match='retained content'):U.publish(folder,root)


def test_failed_publish_keeps_current_pointer_and_removes_only_new_files(tmp_path,payload,monkeypatch):
    root,folder=project(tmp_path,payload)
    original=(root/'data/current-reference.json').read_bytes()
    monkeypatch.setattr(V,'validate_revision',lambda *args:['invalid candidate'])
    with pytest.raises(ValueError,match='invalid candidate'):U.publish(folder,root)
    assert (root/'data/current-reference.json').read_bytes()==original
    assert not list((root/'data/rulesets').glob('wowhead-*'))


def test_current_reference_cannot_select_experiment_or_missing_revision(tmp_path,payload):
    root,_=project(tmp_path,payload)
    assert V.validate_current_reference(root,{('reference',1):(None,{'kind':'baseline','classes':list(W.TREES)})})==[]
    assert V.validate_current_reference(root,{('reference',1):(None,{'kind':'experiment','classes':list(W.TREES)})})
    assert V.validate_current_reference(root,{})


def test_cached_icon_integrity_and_html_response_rejection(tmp_path,payload):
    root,folder=project(tmp_path,payload)
    (root/'web/public/icons/ability_test.jpg').unlink()
    docs=W.convert(payload,W.verify_bundle(folder))
    calls=[]
    def get(url,limit):
        calls.append(url);return jpeg()
    W.prepare_icons(docs,folder,root,get,delay=0)
    assert len(calls)==1 and W.cached_icon(folder,'ability_test.jpg')==jpeg()
    W.prepare_icons(docs,folder,root,get,delay=0)
    assert len(calls)==1
    (folder/'icons/ability_test.jpg').write_bytes(b'corrupted')
    with pytest.raises(ValueError,match='checksum'):W.prepare_icons(docs,folder,root,get,delay=0)
    (folder/'icons/ability_test.jpg').unlink()
    with pytest.raises(ValueError):W.prepare_icons(docs,folder,root,lambda *args:b'<html>blocked</html>',delay=0)


def test_same_source_after_fresh_fetch_retains_original_import_date(tmp_path,payload):
    root,folder=project(tmp_path,payload)
    target=U.publish(folder,root)
    original_pointer=(root/'data/current-reference.json').read_bytes()
    source=V.read(folder/'source.json')
    source['retrievedAt']='2026-11-14T12:00:00Z'
    (folder/'source.json').write_text(json.dumps(source))
    assert U.publish(folder,root)==target
    assert (root/'data/current-reference.json').read_bytes()==original_pointer
