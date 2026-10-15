"""Alternate bit interpretations remain separate, explicit and header backed."""
import copy
import json

import pytest
from pydantic import ValidationError

from conftest import ROOT, require_tool
from praxis.adapters.discovery import parse_cmsis_headers
from praxis.adapters.manual import prepare
from praxis.bundle import Bundle
from praxis.compiler import compile_bundle
from praxis.contracts import load_contract
from praxis.definitions import load_definitions
from praxis.errors import PraxisError
from praxis.models import BitField, FieldView, OperatingMode, Peripheral, PeripheralDiscovery, Profile, Register, SourceRef
from praxis.render import peripheral
from praxis.reports import read_report

REF = SourceRef(source='header', locator='declared symbol')
HEADER = '''typedef struct { unsigned int CTRL; unsigned int DATA; } Block_Type;
#define UNIT_BASE 0x40000000UL
#define UNIT ((Block_Type *) UNIT_BASE)
#define BLOCK_CTRL_SELECT_Msk 0x3UL
#define BLOCK_CTRL_SEND_Msk 0xCUL
#define BLOCK_CTRL_RECEIVE_Msk 0x3CUL
#define BLOCK_CTRL_SHARED_Msk 0x40UL
#define BLOCK_CTRL_SEND_ALIAS_Msk BLOCK_CTRL_SEND_Msk
'''
OPTIONS = dict(structures={'serial': 'Block_Type'}, prefixes={'serial': 'BLOCK'}, stm32_views=False,
               field_views={'serial': {'CTRL': {'transmit': ['SELECT', 'SEND'],
                                                'receive': ['SELECT', 'RECEIVE']}}})


def field(name='SEND', mask=12, lsb=2, width=2):
    return BitField(name=name, mask=mask, lsb=lsb, width=width, meaning='Reviewed test meaning', sources=[REF])


def register(**kwargs):
    return Register.model_validate(dict(name='CTRL', offset=0, width=32, access='RW', access_widths=[32],
        side_effects='Test model only', sources=[REF], field_views={
            'transmit': FieldView(selection='SELECT=0', fields=[field()], sources=[REF]),
            'receive': FieldView(selection='SELECT=1', fields=[field('RECEIVE', 60, 2, 4)], sources=[REF])}, **kwargs))


def entity(reg=None, views=None, fields=None):
    return Peripheral(id='serial', title='Synthetic block', instances=[dict(name='UNIT', base_address=0,
        bus='test', clock='test', sources=[REF])], registers=[reg or register()], reviewed_markdown='test.md',
        review=dict(status='reviewed', reviewer='synthetic test', basis='unit fixture'), operating_modes={
            'send': dict(title='Send test', instances=['UNIT'], registers=['CTRL'], fields=fields or {'CTRL':['SEND']},
                         field_views={'CTRL':'transmit'} if views is None else views,
                         requirements=['Select before enable'], sources=[REF])})


def test_overlap_is_valid_across_views_but_not_within_one_view():
    reg = register()
    assert [f.name for f in reg.fields_for('receive')] == ['RECEIVE']
    assert reg.fields_for() == []
    raw = reg.model_dump()
    raw['field_views']['transmit']['fields'].append(field('WRONG', 4, 2, 1).model_dump())
    with pytest.raises(ValidationError, match='overlapping'):
        Register.model_validate(raw)
    raw = reg.model_dump()
    raw['fields'] = [field('COMMON',4,2,1).model_dump()]
    with pytest.raises(ValidationError, match='overlapping'):
        Register.model_validate(raw)


@pytest.mark.parametrize('views,fields,error', [
    ({}, {'CTRL':['SEND']}, 'must select'),
    ({'CTRL':'absent'}, {'CTRL':['SEND']}, 'undeclared register field view'),
    ({'CTRL':'transmit'}, {'CTRL':['RECEIVE']}, 'undeclared bit field'),
    ({'DATA':'transmit'}, {'CTRL':['SEND']}, 'must name required registers'),
])
def test_mode_cannot_omit_or_mix_interpretations(views, fields, error):
    with pytest.raises(ValidationError, match=error):
        entity(views=views, fields=fields)


def test_common_fields_are_included_in_selected_view_and_masks_are_bounded():
    reg = register(fields=[field('SHARED',64,6,1)], write_mask=124)
    assert [f.name for f in reg.fields_for('receive')] == ['SHARED','RECEIVE']
    entity(reg, fields={'CTRL':['SEND','SHARED']})
    with pytest.raises(ValidationError, match='field envelope'):
        register(write_mask=128)
    raw = reg.model_dump()
    raw['field_views']['receive']['fields'] = [field('BIG',0x10000,16,1).model_dump()]
    raw['width'] = 8
    with pytest.raises(ValidationError, match='out-of-range'):
        Register.model_validate(raw)


def test_empty_additions_preserve_historical_serialized_hash_inputs():
    reg = Register(name='CTRL', offset=0, width=32, access='unknown', side_effects='Unknown', sources=[REF])
    mode = OperatingMode(title='Synthetic mode', instances=['UNIT'], registers=['CTRL'],
                         requirements=['test'], sources=[REF])
    spec = PeripheralDiscovery(structure='Block_Type')
    for record in [reg, mode, spec]:
        assert 'field_views' not in record.model_dump()
        assert 'field_views' not in json.loads(record.model_dump_json())


def discover(tmp_path, options=None):
    require_tool('clang')
    require_tool('arm-none-eabi-gcc')
    header = tmp_path / 'source.h'
    header.write_text(HEADER)
    return parse_cmsis_headers(header, **(OPTIONS if options is None else options))['serial']


def test_generic_adapter_keeps_every_selected_mask_in_its_own_namespace(tmp_path):
    found = discover(tmp_path)
    reg = found.registers[0]
    assert reg.fields == []
    assert [(f.name,f.mask) for f in reg.field_views['receive'].fields] == [('SELECT',3),('RECEIVE',60)]
    assert found.field_expressions['serial.CTRL.transmit.SEND'] == 'BLOCK_CTRL_SEND_Msk'
    assert found.field_expressions['serial.CTRL.receive.RECEIVE'] == 'BLOCK_CTRL_RECEIVE_Msk'
    assert not found.unresolved_masks
    assert reg.access == 'unknown' and reg.access_widths == []
    assert reg.field_views['receive'].fields[1].sources[0].locator == 'BLOCK_CTRL_RECEIVE_Msk'


@pytest.mark.parametrize('views,error', [
    ({'CTRL':{'read':['MISSING']}},'MISSING_DECLARATION'),
    ({'CTRL':{'read':['SEND','RECEIVE']}},'AMBIGUOUS_MASK'),
    ({'NO_REGISTER':{'read':['SEND']}},'MISSING_DECLARATION'),
    ({'CTRL':{}},'INVALID_PROFILE'),
    ({'CTRL':{'read':[]}},'INVALID_PROFILE'),
    ({'CTRL':{'read':['SEND','SEND']}},'INVALID_PROFILE'),
    ({'CTRL':{'read':['SEND_ALIAS']}},'MISSING_DECLARATION'),
])
def test_explicit_view_errors_cannot_be_relaxed_away(tmp_path, views, error):
    options = {**OPTIONS, 'relaxed':True, 'field_views':{'serial':views}}
    with pytest.raises(PraxisError, match=error):
        discover(tmp_path, options)


def test_conflicting_legacy_selection_is_rejected_by_profile_and_adapter(tmp_path):
    with pytest.raises(ValidationError, match='both a legacy'):
        PeripheralDiscovery(structure='Block_Type', register_fields={'CTRL':['SEND']},
                            field_views={'CTRL':{'transmit':['SEND']}})
    with pytest.raises(PraxisError, match='conflicting field selection'):
        discover(tmp_path, {**OPTIONS,'register_fields':{'serial':{'CTRL':['SEND']}}})


def test_manual_candidates_preserve_all_matching_view_names_and_missing_fields(tmp_path):
    declaration = discover(tmp_path)
    parts = [dict(locator='page:1',artifact='part.json',artifact_sha256='0'*64,
                  text='1.1 Mode (BLOCK_CTRL)\nBits 5:2 RECEIVE: receive bits\nBits 1:0 SELECT: selector', tables=[])]
    packet = prepare(declaration, parts, entity='serial', target={}, source={},
                     discovery=PeripheralDiscovery(structure='Block_Type',prefix='BLOCK'))
    candidate = next(c for c in packet['candidates'] if c['field']=='RECEIVE')
    assert candidate['field_views'] == ['receive'] and candidate['status']=='matches_declaration'
    shared = next(c for c in packet['candidates'] if c['field']=='SELECT')
    assert shared['field_views'] == ['receive','transmit']
    assert packet['gaps']['CTRL']['missing_view_field_positions']['transmit'] == ['SEND']
    assert not packet['publication_ready']


def test_manual_same_name_with_different_view_masks_remains_an_explicit_gap(tmp_path):
    declaration = discover(tmp_path)
    raw = declaration.model_dump()
    views = raw['registers'][0]['field_views']
    views['receive']['fields'][1]['name'] = 'SEND'
    from praxis.adapters.discovery import Declaration
    declaration = Declaration.model_validate(raw)
    packet = prepare(declaration,[dict(locator='page:1',artifact='part.json',artifact_sha256='0'*64,
        text='1.1 Mode (BLOCK_CTRL)\nBits 5:2 SEND: ambiguous view',tables=[])],
        entity='serial',target={},source={},discovery=PeripheralDiscovery(structure='Block_Type',prefix='BLOCK'))
    assert packet['candidates']==[]
    assert packet['extraction_issues'][0]['code']=='AMBIGUOUS_FIELD_VIEW'
    assert packet['gaps']['CTRL']['missing_view_field_positions']['receive']==['SELECT','SEND']


def test_markdown_keeps_contiguous_tables_and_explicit_mode_selection():
    item = entity()
    target = Bundle(ROOT/'bundles/stm32f401re').manifest.target
    text = peripheral(target,item,'Synthetic reviewed narrative')
    assert '### CTRL: receive' in text and '### CTRL: transmit' in text
    assert '| CTRL | RECEIVE | 5:2 | 0x3C |' in text
    assert '| CTRL | SEND | 3:2 | 0xC |' in text
    assert 'Selected register field views' in text and 'CTRL: transmit' in text


@pytest.fixture(scope='module')
def timer_bundle(tmp_path_factory):
    require_tool('clang')
    require_tool('arm-none-eabi-gcc')
    return Bundle(compile_bundle(ROOT/'sources/stm32f407g-disc1/profile-timer-views-v1.json',
                                tmp_path_factory.mktemp('timer-views')/'bundle'))


def test_f407_full_and_mixed_channel_declarations_do_not_invent_ready_modes(timer_bundle):
    text = timer_bundle.read('wiki/peripherals/tim.md')
    for reg in ('CCMR1','CCMR2'):
        for view in ('input_input','input_output','output_input','output_output'):
            assert f'### {reg}: {view}' in text
    for field_name in ('IC1PSC','IC1F','IC2PSC','IC2F','IC3PSC','IC3F','IC4PSC','IC4F'):
        assert f'| {field_name} |' in text
    report = read_report(timer_bundle,'coverage')
    assert report['counts']['reviewed_subsets'] == 22
    assert sum(row['ready'] for row in report['workflows'].values()) == 20
    assert report['workflows']['uart_timer_interrupts']['ready']
    assert 'pwm_ch1' not in report['peripherals']['tim']['reviewed_modes']
    assert report['peripherals']['tim']['field_view_rows'] == 64


def test_f407_new_view_bundle_is_byte_identical_on_repeated_compilation(timer_bundle,tmp_path):
    other = Bundle(compile_bundle(ROOT/'sources/stm32f407g-disc1/profile-timer-views-v1.json',tmp_path/'bundle'))
    assert other.manifest.bundle_revision == timer_bundle.manifest.bundle_revision
    assert other.manifest.file_hashes == timer_bundle.manifest.file_hashes


def test_no_accidental_mutation_of_operating_mode_data():
    original = entity()
    raw = copy.deepcopy(original.model_dump())
    raw['operating_modes']['send']['field_views']['CTRL'] = 'receive'
    with pytest.raises(ValidationError,match='undeclared bit field'):
        Peripheral.model_validate(raw)
    assert original.operating_modes['send'].field_views == {'CTRL':'transmit'}


def test_recorded_f407_mcp_packet_preserves_unreviewed_access_and_source_integrity():
    from praxis.adapters.manual import canonical
    from praxis.bundle import digest
    path = ROOT/'examples/inventory/stm32f407g-disc1/timer-views-review.json'
    packet = json.loads(path.read_text())
    checksum = packet.pop('packet_sha256')
    assert digest(canonical(packet)) == checksum
    assert packet['counts']['candidates'] == 32 and not packet['conflicts']
    assert not packet['publication_ready'] and packet['review_required']
    for gap in packet['gaps'].values():
        assert gap['missing_categories'] == ['access']
        assert all(not values for values in gap['missing_view_field_positions'].values())
    for fact in packet['candidates']:
        if fact['kind']=='field':
            assert fact['status']=='matches_declaration' and fact['field_views']
        if fact['kind']=='reset':
            assert fact['status']=='unreviewed'
    profile = ROOT/'sources/stm32f407g-disc1/profile-timer-views-v1.json'
    assert packet['source']['profile_sha256'] == digest(profile.read_bytes())


@pytest.fixture(scope='module')
def compilation_inputs():
    require_tool('clang')
    require_tool('arm-none-eabi-gcc')
    from praxis.coverage import inventory
    root = ROOT/'sources/stm32f407g-disc1'
    profile = Profile.model_validate_json((root/'profile-timer-views-v1.json').read_bytes())
    paths = {s.id:root/s.path for s in profile.sources}
    items = load_definitions(profile,paths)
    catalog,entries = inventory(profile,paths,items,root)
    return root,profile,paths,items,catalog,entries


def reviewed_inputs(inputs):
    root,profile,paths,items,catalog,entries = inputs
    tim = next(item for item in items if item.id=='tim')
    declared = next(r for r in catalog['tim'].registers if r.name=='CCMR1')
    raw = declared.model_dump()
    raw.update(access='RW',access_widths=[32])
    raw['field_views']['input_input']['selection'] = 'Synthetic editorial test condition'
    registers = [r.model_dump() for r in tim.registers if r.name!='CCMR1']+[raw]
    updated = Peripheral.model_validate({**tim.model_dump(),'registers':registers})
    return [updated if item.id=='tim' else item for item in items]


@pytest.mark.parametrize('change', ['mask','name','view'])
def test_reviewed_view_conflicts_block_compiler_merge(compilation_inputs,monkeypatch,change):
    from praxis.compiler import _discover
    root,profile,paths,_,catalog,entries = compilation_inputs
    items = reviewed_inputs(compilation_inputs)
    raw = next(i for i in items if i.id=='tim').model_dump()
    reg = next(r for r in raw['registers'] if r['name']=='CCMR1')
    if change=='view':
        reg['field_views']['absent'] = reg['field_views'].pop('input_input')
    else:
        f = next(f for f in reg['field_views']['input_input']['fields'] if f['name']=='IC1F')
        f.update({'mask':0x70,'width':3} if change=='mask' else {'name':'INVENTED'})
    items = [Peripheral.model_validate(raw) if i.id=='tim' else i for i in items]
    monkeypatch.setattr('praxis.coverage.inventory',lambda *args:(catalog,entries))
    with pytest.raises(PraxisError,match='DECLARATION_CONFLICT'):
        _discover(profile,paths,items,root,load_contract(profile,root))


def test_reviewed_view_meaning_merges_without_changing_other_views(compilation_inputs,monkeypatch):
    from praxis.compiler import _discover
    root,profile,paths,_,catalog,entries = compilation_inputs
    items = reviewed_inputs(compilation_inputs)
    monkeypatch.setattr('praxis.coverage.inventory',lambda *args:(catalog,entries))
    merged,_,_ = _discover(profile,paths,items,root,load_contract(profile,root))
    reg = next(r for i in merged if i.id=='tim' for r in i.registers if r.name=='CCMR1')
    assert reg.field_views['input_input'].selection == 'Synthetic editorial test condition'
    assert reg.field_views['output_output'].selection.startswith('Configured declaration set only')


@pytest.mark.parametrize('fault', ['unknown_view_source','unknown_field_source','unreviewed_selection'])
def test_view_provenance_and_selection_authority_are_checked(compilation_inputs,monkeypatch,fault):
    from praxis.compiler import _definitions
    root,profile,paths,_,_,_ = compilation_inputs
    items = reviewed_inputs(compilation_inputs)
    raw = next(i for i in items if i.id=='tim').model_dump()
    reg = next(r for r in raw['registers'] if r['name']=='CCMR1')
    view = reg['field_views']['input_input']
    if fault=='unknown_view_source':
        view['sources'] = [dict(source='absent',locator='test')]
    elif fault=='unknown_field_source':
        view['fields'][0]['sources'] = [dict(source='absent',locator='test')]
    else:
        reg['sources'].append(dict(source='rm_tim_cr1',locator='synthetic test only'))
        raw['operating_modes']['capture_fixture'] = dict(title='Synthetic test only',instances=['TIM2'],
            registers=['CCMR1'],field_views={'CCMR1':'input_input'}, requirements=['test'],
            sources=[dict(source='rm_tim_cr1',locator='synthetic test only')])
    items = [Peripheral.model_validate(raw) if i.id=='tim' else i for i in items]
    monkeypatch.setattr('praxis.definitions.load_definitions',lambda *args:items)
    with pytest.raises(PraxisError,match='SOURCE_AUTHORITY' if fault=='unreviewed_selection' else 'UNKNOWN_SOURCE'):
        _definitions(profile,paths,root)
