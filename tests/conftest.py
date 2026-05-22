from dataclasses import dataclass
from typing import Protocol

import pytest

from base_cli import main


@dataclass(frozen=True, slots=True)
class CliResult:
    code: int
    stdout: str
    stderr: str


class RunCli(Protocol):
    def __call__(self, *args: str) -> CliResult: ...


@pytest.fixture
def run_cli(capsys: pytest.CaptureFixture[str]) -> RunCli:
    def _run(*args: str) -> CliResult:
        try:
            code = main.main(list(args))
        except SystemExit as exc:
            # argparse always exits with an int status
            code = exc.code if isinstance(exc.code, int) else 1  # pragma: no branch
        captured = capsys.readouterr()
        return CliResult(code=code, stdout=captured.out, stderr=captured.err)

    return _run
