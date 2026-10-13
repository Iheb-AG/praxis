"""Broader CMSIS extraction, honest readiness, generic DAGs and immutable publication."""
import asyncio
import json
import shutil
import sys

import pytest
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from praxis.adapters.headers import cmsis
from praxis.bundle import Bundle
from praxis.cli import main
from praxis.compiler import compile_bundle, parse_cmsis_headers
from praxis.coverage import order
from praxis.errors import PraxisError
from praxis.evaluation import evaluate
from praxis.models import MAX_DOCUMENT_BYTES
from praxis.routing import Session
from conftest import ROOT, require_tool

SOURCE = ROOT / 'sources/stm32f407g-disc1'


@pytest.fixture(scope='module')
def broad(tmp_path_factory):
    require_tool('clang')
    require_tool('arm-none-eabi-gcc')
    path = compile_bundle(SOURCE / 'profile-discovery.json', tmp_path_factory.mktemp('broad') / 'bundle')
    return Bundle(path)


def coverage(bundle):
    return json.loads(bundle.read('wiki/coverage.md').split('```json\n')[1].split('\n```')[0])


def test_whole_header_inventory_and_readiness(broad):
    report = coverage(broad)
    assert broad.manifest.schema_version == 2
    assert {'tim', 'spi', 'i2c', 'dma_stream', 'can', 'adc', 'rtc', 'exti', 'syscfg', 'usb_otg_global'} <= broad.manifest.peripherals.keys()
    assert report['counts']['published'] > 30
    assert report['counts']['reviewed_subsets'] == 4
    assert report['peripherals']['itm']['status'] == 'blocked'
    assert report['peripherals']['usb_otg_inendpoint']['status'] == 'unmapped_type'
    assert report['peripherals']['flash']['status'] == 'partial_declarations'
    assert 'bit fields withheld' in broad.read('wiki/peripherals/flash.md')
    assert report['workflows']['gpio_led_button']['ready']
    assert not report['workflows']['uart_timer_interrupts']['ready']
    assert any('tim: operating semantics not reviewed' in issue
               for issue in report['workflows']['uart_timer_interrupts']['issues'])
    assert report['sources']['profile']['sha256']
    assert report['source_catalog'] == '[[sources]]'
    assert set(report['sources']) == {'profile'}
    assert len(broad.manifest.sources) > len(report['sources'])
    assert all(len(text.encode()) <= MAX_DOCUMENT_BYTES for text in broad.documents.values())
    assert 'declarations only' in broad.read('wiki/peripherals/tim.md')
    assert 'Not reviewed.' in broad.read('wiki/peripherals/tim.md')
    assert broad.manifest.aliases['tim2'] == 'tim'
    assert broad.manifest.aliases['dma1_stream0'] == 'dma_stream'


def test_branch_dependencies_do_not_require_unrelated_uart(broad):
    session = Session(broad)
    session.read_wiki_index()
    with pytest.raises(PraxisError, match='retrieve in order: rcc, gpio, syscfg'):
        session.read_peripheral_doc('exti')
    for name in ('rcc', 'gpio', 'syscfg', 'exti', 'tim2', 'spi1', 'dma', 'dma1_stream0'):
        assert session.read_peripheral_doc(name)
    assert 'usart' not in session.served and 'nvic' not in session.served
    assert broad.dependencies['dma_stream'] == ['dma']
    assert evaluate(broad)['passed']


def test_nested_can_layouts_and_dma_stream_masks(broad):
    can = broad.read('wiki/peripherals/can.md')
    assert 'sTxMailBox_0__TIR' in can
    assert '0x180' in can and 'sFilterRegister_27__FR2' in can
    stream = broad.read('wiki/peripherals/dma_stream.md')
    assert 'DMA_SxCR_EN_Msk' in stream
    assert 'USB_OTG_FS_PERIPH_BASE + USB_OTG_GLOBAL_BASE' in broad.read('wiki/peripherals/usb_otg_global.md')


def test_custom_structure_and_prefix(tmp_path):
    require_tool('arm-none-eabi-gcc')
    header = tmp_path / 'new.h'
    header.write_text('''typedef struct { unsigned int CTRL; unsigned int RESERVED[3];
    struct { unsigned char DATA[4]; } CHANNEL[2]; } NEW_TypeDef;
#define NEW0_BASE (0x40000000UL + 0x400UL)
#define NEW0 ((NEW_TypeDef *) NEW0_BASE)
#define NOVEL_CTRL_ENABLE_Pos 2U
#define NOVEL_CTRL_ENABLE_Msk (1UL << NOVEL_CTRL_ENABLE_Pos)
''')
    found = parse_cmsis_headers(header, structures={'novel': 'NEW_TypeDef'},
                               prefixes={'novel': 'NOVEL'}, relaxed=True)['novel']
    assert found.instances['NEW0'] == 0x40000400
    assert found.registers[0].fields[0].mask == 4
    assert [(r.offset, r.count, r.width) for r in found.registers[1:]] == [(16, 4, 8), (20, 4, 8)]
    assert found.members['CHANNEL_1__DATA'] == 'CHANNEL[1].DATA'


def test_unsupported_union_is_explicit(tmp_path):
    header = tmp_path / 'union.h'
    header.write_text('typedef struct { union { unsigned int W; unsigned char B; } PORT; } Odd_TypeDef;')
    failures = {}
    assert cmsis(header, None, [], failures=failures) == {}
    assert 'Unsupported nested member: PORT' in failures['Odd_TypeDef']


def test_explicit_array_expansion_and_overlapping_field_views(tmp_path):
    require_tool('arm-none-eabi-gcc')
    header = tmp_path / 'views.h'
    header.write_text('''typedef struct { unsigned int ROUTE[2]; unsigned int MODE; } VIEW_TypeDef;
#define VIEW0_BASE 0x40000000UL
#define VIEW0 ((VIEW_TypeDef *) VIEW0_BASE)
#define VIEW_ROUTE1_PIN_Msk 0xFUL
#define VIEW_ROUTE2_PIN_Msk 0xF0UL
#define VIEW_MODE_INPUT_Msk 0xFUL
#define VIEW_MODE_OUTPUT_Msk 0x7UL
''')
    options = dict(structures={'view': 'VIEW_TypeDef'}, expand_arrays={'view': ['ROUTE']},
        register_prefixes={'view': {'ROUTE0': 'VIEW_ROUTE1', 'ROUTE1': 'VIEW_ROUTE2'}},
        register_fields={'view': {'MODE': ['OUTPUT']}})
    result = parse_cmsis_headers(header, **options)['view']
    assert [(r.name, r.offset, r.count) for r in result.registers] == [
        ('ROUTE0', 0, 1), ('ROUTE1', 4, 1), ('MODE', 8, 1)]
    assert result.members['ROUTE1'] == 'ROUTE[1]'
    assert result.registers[-1].fields[0].mask == 7
    for fields in [{'MODE': ['MISSING']}, {'MODE': ['OUTPUT'], 'UNKNOWN': ['OUTPUT']}]:
        with pytest.raises(PraxisError, match='MISSING_DECLARATION'):
            parse_cmsis_headers(header, **{**options, 'register_fields': {'view': fields}})
    with pytest.raises(PraxisError, match='AMBIGUOUS_MASK'):
        parse_cmsis_headers(header, **{**options, 'register_fields': {}})


def test_graph_rejects_cycles_and_dangling_dependencies():
    with pytest.raises(PraxisError, match='DEPENDENCY_CYCLE'):
        order({'tim': ['gpio'], 'gpio': ['tim']})
    with pytest.raises(PraxisError, match='Unknown prerequisite'):
        order({'tim': ['not_published']})
    assert order({'tim': ['rcc'], 'spi': ['rcc'], 'rcc': []}) == ['rcc', 'spi', 'tim']


def test_determinism_across_locations(broad, tmp_path):
    source = tmp_path / 'sources'
    shutil.copytree(SOURCE, source, ignore=shutil.ignore_patterns("imports"))
    other = compile_bundle(source / 'profile-discovery.json', tmp_path / 'other')
    assert Bundle(other).manifest.bundle_revision == broad.manifest.bundle_revision
    for path in ['manifest.json', *broad.documents]:
        assert (other / path).read_bytes() == (broad.root / path).read_bytes()


def test_required_unreviewed_workflow_blocks_publication_but_report_works(tmp_path, capsys):
    source = tmp_path / 'source'
    shutil.copytree(SOURCE, source, ignore=shutil.ignore_patterns("imports"))
    path = source / 'profile-discovery.json'
    data = json.loads(path.read_text())
    data['publication_requires'].append('uart_timer_interrupts')
    path.write_text(json.dumps(data))
    output = tmp_path / 'rejected'
    with pytest.raises(PraxisError, match='PUBLICATION_BLOCKED'):
        compile_bundle(path, output)
    assert not output.exists()
    assert main(['coverage', '--profile', str(path)]) == 0
    report = json.loads(capsys.readouterr().out)
    assert not report['publication_ready']
    assert not report['workflows']['uart_timer_interrupts']['ready']


def test_explicit_selection_unknown_dependency_and_duplicate_structure(tmp_path):
    source = tmp_path / 'source'
    shutil.copytree(SOURCE, source, ignore=shutil.ignore_patterns("imports"))
    path = source / 'profile-discovery.json'
    data = json.loads(path.read_text())
    data['discovery']['automatic'] = False
    data['discovery']['peripherals'] = {'timer': {'structure': 'TIM_TypeDef', 'prerequisites': ['gpio']}}
    path.write_text(json.dumps(data))
    bundle = Bundle(compile_bundle(path, tmp_path / 'selected'))
    assert set(bundle.manifest.peripherals) == {'rcc', 'gpio', 'usart', 'nvic', 'timer'}
    assert bundle.manifest.aliases['tim2'] == 'timer'
    assert coverage(bundle)['peripherals']['spi']['status'] == 'not_selected'
    data['discovery']['peripherals']['timer']['prerequisites'] = ['missing']
    path.write_text(json.dumps(data))
    with pytest.raises(PraxisError, match='Unknown prerequisite'):
        compile_bundle(path, tmp_path / 'bad')
    data['discovery']['peripherals']['duplicate'] = {'structure': 'TIM_TypeDef'}
    path.write_text(json.dumps(data))
    with pytest.raises(PraxisError, match='DUPLICATE_ENTITY'):
        compile_bundle(path, tmp_path / 'dup')


async def test_real_stdio_dynamic_dependencies(broad, tmp_path):
    async def exercise():
        params = StdioServerParameters(command=sys.executable,
            args=[str(ROOT / 'server.py'), '--bundle', str(broad.root)], cwd=str(tmp_path))
        async with stdio_client(params) as (reader, writer), ClientSession(reader, writer) as client:
            await client.initialize()
            await client.call_tool('read_wiki_index', {})
            blocked = await client.call_tool('read_peripheral_doc', {'peripheral_name': 'tim2'})
            assert blocked.isError and 'rcc' in blocked.content[0].text
            for entity in ('rcc', 'tim2', 'i2c1'):
                result = await client.call_tool('read_peripheral_doc', {'peripheral_name': entity})
                assert not result.isError
            assert 'operating semantics are NOT reviewed' in result.content[0].text
    await asyncio.wait_for(exercise(), timeout=30)


@pytest.mark.parametrize('explicit', [False, True])
def test_oversized_automatic_document_reported_but_explicit_document_fails(tmp_path, monkeypatch, explicit):
    import praxis.compiler as compiler
    source = tmp_path / 'source'
    shutil.copytree(SOURCE, source, ignore=shutil.ignore_patterns("imports"))
    profile = source / 'profile-discovery.json'
    if explicit:
        data = json.loads(profile.read_text())
        data['discovery']['peripherals']['tim'] = {'structure': 'TIM_TypeDef'}
        profile.write_text(json.dumps(data))
    render = compiler.peripheral

    def oversized(target, item, narrative):
        return render(target, item, narrative) + ('X' * 65536 if item.id == 'tim' else '')

    monkeypatch.setattr(compiler, 'peripheral', oversized)
    output = tmp_path / 'output'
    if explicit:
        with pytest.raises(PraxisError, match='DOCUMENT_TOO_LARGE'):
            compile_bundle(profile, output)
        assert not output.exists()
    else:
        bundle = Bundle(compile_bundle(profile, output))
        row = coverage(bundle)['peripherals']['tim']
        assert row['status'] == 'blocked' and not row['published']
        assert 'DOCUMENT_TOO_LARGE' in row['issues'][0]
        assert 'tim' not in bundle.manifest.peripherals
        assert not (bundle.root / 'wiki/peripherals/tim.md').exists()
