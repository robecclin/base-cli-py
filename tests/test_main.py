import pytest

from base_cli import main


def test_main_dispatches_subcommand(capsys: pytest.CaptureFixture[str]) -> None:
    rc = main.main(["helloworld"])
    assert rc == 0
    assert capsys.readouterr().out == "Hello, world!\n"


def test_main_passes_name_argument(capsys: pytest.CaptureFixture[str]) -> None:
    rc = main.main(["helloworld", "--name", "Alice"])
    assert rc == 0
    assert capsys.readouterr().out == "Hello, Alice!\n"


def test_main_requires_subcommand() -> None:
    with pytest.raises(SystemExit) as exc:
        main.main([])
    assert exc.value.code != 0


def test_main_rejects_unknown_subcommand() -> None:
    with pytest.raises(SystemExit) as exc:
        main.main(["nope"])
    assert exc.value.code != 0


def test_main_help_exits_zero(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as exc:
        main.main(["--help"])
    assert exc.value.code == 0
    assert "base-cli" in capsys.readouterr().out
