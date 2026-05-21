import pytest

from base_cli.command import helloworld


def test_run_with_name(capsys: pytest.CaptureFixture[str]) -> None:
    rc = helloworld.run("Alice")
    assert rc == 0
    assert capsys.readouterr().out == "Hello, Alice!\n"
