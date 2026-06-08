from tests.conftest import RunCli


def test_main_dispatches_subcommand(run_cli: RunCli) -> None:
    result = run_cli("helloworld")
    assert result.exit_code == 0
    assert result.stdout == "Hello, world!\n"
    assert result.stderr == ""


def test_main_passes_name_argument(run_cli: RunCli) -> None:
    result = run_cli("helloworld", "--name", "Alice")
    assert result.exit_code == 0
    assert result.stdout == "Hello, Alice!\n"
    assert result.stderr == ""


def test_main_dispatches_goodbye(run_cli: RunCli) -> None:
    result = run_cli("goodbye", "--name", "Bob")
    assert result.exit_code == 0
    assert result.stdout == "Goodbye, Bob!\n"
    assert result.stderr == ""


def test_main_requires_subcommand(run_cli: RunCli) -> None:
    result = run_cli()
    assert result.exit_code == 2
    assert "Usage:" in result.stdout
    assert "helloworld" in result.stdout
    assert "goodbye" in result.stdout
    assert result.stderr == ""


def test_main_rejects_unknown_subcommand(run_cli: RunCli) -> None:
    result = run_cli("unknown")
    assert result.exit_code == 2
    assert result.stdout == ""
    assert "No such command 'unknown'." in result.stderr


def test_main_help_exits_zero(run_cli: RunCli) -> None:
    result = run_cli("--help")
    assert result.exit_code == 0
    assert "helloworld" in result.stdout
    assert "goodbye" in result.stdout
    assert result.stderr == ""
