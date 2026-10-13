"""Compile only the reviewed, repository-owned fixture on the host; never arbitrary agent C."""
import subprocess

import pytest

from conftest import ROOT, require_tool


@pytest.fixture(scope='module')
def clock_models(tmp_path_factory):
    require_tool('gcc')
    out = tmp_path_factory.mktemp('clock-model')
    result = {}
    for name, source in {
        'fixed': ROOT / 'examples/stm32f407g-disc1-led-button/validated_opencode_application/led_button.c',
        'original': ROOT / 'tests/fixtures/f407_led_button_before_clock_fix/led_button.c',
    }.items():
        executable = out / name
        args = ['gcc', '-std=c11', '-Wall', '-Wextra', '-Werror',
                '-I' + str(ROOT / 'tests/fixtures/f407_clock_model'),
                '-DAPP_SOURCE="' + str(source) + '"',
                str(ROOT / 'tests/fixtures/f407_clock_model/harness.c'), '-o', str(executable)]
        if name == 'original':
            args.append('-DORIGINAL_APP')
        compiled = subprocess.run(args, capture_output=True, timeout=20)
        assert compiled.returncode == 0, compiled.stderr.decode()
        result[name] = executable
    return result


@pytest.mark.parametrize('scenario', range(7))
def test_reviewed_application_handles_clock_state_and_failure(clock_models, scenario):
    result = subprocess.run([str(clock_models['fixed']), str(scenario)], capture_output=True, timeout=3)
    assert result.returncode == 0, result.stderr.decode()


def test_original_model_application_fails_prescaler_regression(clock_models):
    result = subprocess.run([str(clock_models['original']), '0'], capture_output=True, timeout=3)
    assert result.returncode != 0
