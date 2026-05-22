from dataclasses import dataclass
from typing import Protocol

import pytest
from typer.testing import CliRunner

from base_cli import main  # pyright: ignore[reportUnusedImport]  # noqa: F401
from base_cli.app import app


@dataclass(frozen=True, slots=True)
class CliResult:
    code: int
    stdout: str


class RunCli(Protocol):
    def __call__(self, *args: str) -> CliResult: ...


@pytest.fixture
def run_cli() -> RunCli:
    runner = CliRunner()

    def _run(*args: str) -> CliResult:
        result = runner.invoke(app, list(args))
        return CliResult(code=result.exit_code, stdout=result.stdout)

    return _run
