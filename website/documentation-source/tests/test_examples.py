import subprocess

import pytest

from conftest import ROOT, require_tool


def compile_checked(args):
    result = subprocess.run(args, cwd=ROOT, capture_output=True, text=True, timeout=30)
    assert result.returncode == 0, result.stdout + result.stderr


@pytest.mark.parametrize("target,compiler,flags", [
    ("stm32f401re", "arm-none-eabi-gcc", ["-mcpu=cortex-m4", "-mthumb", "-mfloat-abi=soft", "-DSTM32F401xE"]),
    ("atmega328p", "avr-gcc", ["-mmcu=atmega328p", "-DF_CPU=16000000UL"]),
])
@pytest.mark.parametrize("mode", ["syntax", "object"])
def test_target_examples_and_header_assertions(tmp_path, target, compiler, flags, mode):
    require_tool(compiler)
    for name in ["polling", "interrupts"]:
        args = [compiler, *flags, "-std=c11", "-ffreestanding", "-Wall", "-Wextra", "-Werror",
                f"-I{ROOT / 'sources' / target / 'raw/vendor'}", f"-I{ROOT / 'examples/include'}",
                "-fsyntax-only" if mode == "syntax" else "-c", str(ROOT / "examples" / target / f"{name}.c")]
        if mode == "object":
            args.extend(["-o", str(tmp_path / f"{name}.o")])
        compile_checked(args)


@pytest.mark.parametrize("target,harness", [("stm32f401re", "stm32_model_test.c"), ("atmega328p", "avr_model_test.c")])
def test_actual_driver_register_values_on_host_models(tmp_path, target, harness):
    require_tool("gcc")
    executable = tmp_path / "model"
    args = ["gcc", "-std=c11", "-Wall", "-Wextra", "-Werror", "-DF_CPU=16000000UL",
            "-Itests/fixtures", "-Iexamples/include", f"tests/fixtures/{harness}",
            f"examples/{target}/polling.c", f"examples/{target}/interrupts.c", "-o", str(executable)]
    compile_checked(args)
    compile_checked([str(executable)])


def test_shared_stage_order_and_failure_short_circuit(tmp_path):
    require_tool("gcc")
    executable = tmp_path / "order"
    compile_checked(["gcc", "-std=c11", "-Wall", "-Wextra", "-Werror", "-Iexamples/include",
                     "examples/model/order_test.c", "-o", str(executable)])
    compile_checked([str(executable)])


@pytest.mark.parametrize("target,bad_value", [("stm32f401re", "PRAXIS_AF = 6"), ("atmega328p", "PRAXIS_UBRR = 104")])
def test_golden_models_catch_wrong_generated_configuration(tmp_path, target, bad_value):
    require_tool("gcc")
    source = (ROOT / "examples" / target / "polling.c").read_text()
    original = "PRAXIS_AF = 7" if target.startswith("stm") else "PRAXIS_UBRR = 103"
    modified = tmp_path / "bad.c"
    modified.write_text(source.replace(original, bad_value))
    harness = "stm32_model_test.c" if target.startswith("stm") else "avr_model_test.c"
    executable = tmp_path / "bad"
    result = subprocess.run(["gcc", "-std=c11", "-DF_CPU=16000000UL", "-Itests/fixtures", "-Iexamples/include",
                             f"tests/fixtures/{harness}", str(modified), f"examples/{target}/interrupts.c",
                             "-o", str(executable)], cwd=ROOT, capture_output=True, timeout=30)
    if result.returncode == 0:
        result = subprocess.run([str(executable)], capture_output=True, timeout=5)
    assert result.returncode != 0

