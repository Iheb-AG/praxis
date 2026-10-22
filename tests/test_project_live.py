"""Live diagnostics use real stdio; fault cases never require hardware access."""
import asyncio
from types import SimpleNamespace

import pytest
from mcp.types import CallToolResult, TextContent

from conftest import ROOT, require_tool
from praxis.errors import PraxisError
from praxis.project_check import check_project
from praxis.project_live import inspect_session, inspect_services, REQUIRED, value
from praxis.project_workspace import create_project


@pytest.fixture
def project(tmp_path):
    require_tool('clang')
    root = tmp_path / 'live-project'
    create_project(root, 'live_check', ROOT / 'sources/stm32f407g-disc1/profile.json',
        ROOT / 'assets/stm32f407vg', ROOT / 'toolchain-f407.lock.json', mode='fresh',
        catalog=ROOT / 'sources/stm32f407g-disc1/web-sources.json', install_codex=True)
    return root


def test_all_four_actual_services_report_same_selection(project):
    report = check_project(project, live=True)
    assert report['configuration_valid'] and report['live_services'] == 'passed', report
    assert len(report['services']) == 4
    assert all(row['status'] == 'passed' for row in report['services'])
    assert report['sandbox_execution'] == 'not_checked'
    assert not list((project / '.praxis/artifacts').iterdir())
    assert not list((project / '.praxis/references').iterdir())


def test_invalid_configuration_never_launches(project, monkeypatch):
    import praxis.project_live
    monkeypatch.setattr(praxis.project_live, 'inspect_services', lambda *a: pytest.fail('Must not launch'))
    config = project / '.codex/config.toml'
    config.write_text(config.read_text().replace('enabled = true', 'enabled = false', 1))
    assert check_project(project, live=True)['live_services'] == 'blocked_by_configuration'


def test_cli_live_failure_returns_nonzero(project, monkeypatch, capsys):
    import praxis.project_live
    from praxis.cli import main

    async def failed(*args):
        return [{'name': 'praxis', 'status': 'failed', 'code': 'MCP_CONNECTION_FAILED'}]

    monkeypatch.setattr(praxis.project_live, 'inspect_services', failed)
    assert main(['project-check', '--root', str(project), '--live']) == 1
    assert 'MCP_CONNECTION_FAILED' in capsys.readouterr().out


def test_live_selection_change_cannot_report_success(project, monkeypatch):
    import praxis.project_live
    from praxis.handoff import BundleHandoff
    original = BundleHandoff.selection
    changed = False

    def selection(self):
        result = original(self)
        return result.model_copy(update={'generation': result.generation + 1}) if changed else result

    async def successful(*args):
        nonlocal changed
        changed = True
        return [{'name': n, 'status': 'passed'} for n in REQUIRED]

    monkeypatch.setattr(BundleHandoff, 'selection', selection)
    monkeypatch.setattr(praxis.project_live, 'inspect_services', successful)
    report = check_project(project, live=True)
    assert report['live_services'] == 'failed'
    assert report['checks'][-1]['code'] == 'SELECTION_CHANGED'


@pytest.mark.parametrize('timeout', [0, -1, 121, float('nan'), float('inf')])
def test_timeout_bounds(tmp_path, timeout):
    with pytest.raises(PraxisError, match='INVALID_INPUT'):
        check_project(tmp_path, live=True, timeout=timeout)


class FakeSession:
    def __init__(self, names, response):
        self.names, self.response, self.calls = names, response, []

    async def initialize(self):
        pass

    async def list_tools(self, cursor=None):
        return SimpleNamespace(tools=[SimpleNamespace(name=n) for n in self.names], nextCursor=None)

    async def call_tool(self, name, arguments):
        self.calls.append(name)
        return CallToolResult(content=[], structuredContent=self.response)


@pytest.mark.parametrize('fault,code', [('missing', 'MCP_TOOLS_MISSING'),
    ('write', 'UNEXPECTED_HARDWARE_AUTHORITY'), ('duplicate', 'MCP_CATALOG_INVALID'),
    ('revision', 'MCP_REVISION_MISMATCH'), ('response', 'MCP_RESPONSE_INVALID')])
async def test_bad_build_catalog_or_revision_rejected(fault, code, tmp_path):
    names = list(REQUIRED['praxis_build'])
    if fault == 'missing':
        names.remove('validate_firmware')
    elif fault == 'write':
        names.append('flash_firmware')
    elif fault == 'duplicate':
        names.append(names[0])
    target = SimpleNamespace(model_dump=lambda: {'id': 'expected'})
    bundle = SimpleNamespace(manifest=SimpleNamespace(target=target))
    selection = SimpleNamespace(bundle_revision='expected', generation=0)
    session = FakeSession(names, {'result': 'bad'} if fault == 'response' else {'target': {'id': 'wrong'}})
    with pytest.raises(PraxisError, match=code):
        await inspect_session(session, 'praxis_build', bundle, selection, tmp_path)
    assert set(session.calls) <= {'get_build_profile'}


async def test_timeout_cleanup_and_other_services_continue(monkeypatch, tmp_path):
    from contextlib import asynccontextmanager
    import praxis.project_live as live
    entered, closed = [], []

    @asynccontextmanager
    async def stalled(params, errlog):
        entered.append(params.command)
        try:
            await asyncio.sleep(60)
            yield None
        finally:
            closed.append(params.command)

    monkeypatch.setattr(live, 'stdio_client', stalled)
    entries = {name: {'command': name, 'args': [], 'cwd': str(tmp_path)} for name in REQUIRED}
    results = await inspect_services(entries, None, None, tmp_path, .01)
    assert entered == closed == list(REQUIRED)
    assert all(row['code'] == 'MCP_TIMEOUT' for row in results)


def test_text_result_and_tool_error():
    assert value(CallToolResult(content=[TextContent(type='text', text='index body')])) == 'index body'
    with pytest.raises(PraxisError, match='MCP_TOOL_ERROR'):
        value(CallToolResult(isError=True, content=[TextContent(type='text', text='blocked')]))
