from importlib.metadata import version

from tests.conftest import RunCli


def test_main_dispatches_subcommand(run_cli: RunCli) -> None:
    result = run_cli("helloworld")
    assert result.code == 0
    assert result.stdout == "Hello, world!\n"


def test_main_passes_name_argument(run_cli: RunCli) -> None:
    result = run_cli("helloworld", "--name", "Alice")
    assert result.code == 0
    assert result.stdout == "Hello, Alice!\n"


def test_main_requires_subcommand(run_cli: RunCli) -> None:
    assert run_cli().code != 0


def test_main_rejects_unknown_subcommand(run_cli: RunCli) -> None:
    assert run_cli("nope").code != 0


def test_main_help_exits_zero(run_cli: RunCli) -> None:
    result = run_cli("--help")
    assert result.code == 0
    assert "base-cli" in result.stdout


def test_main_version_exits_zero(run_cli: RunCli) -> None:
    result = run_cli("--version")
    assert result.code == 0
    assert result.stdout == f"base-cli {version('base-cli')}\n"
