import logging

from rich.markdown import Markdown

from base_cli.logging import MarkdownRichHandler
from tests.conftest import RunCli


def test_default_verbosity_is_info(run_cli: RunCli) -> None:
    run_cli("helloworld")
    assert logging.getLogger().level == logging.INFO


def test_verbose_flag_sets_debug(run_cli: RunCli) -> None:
    run_cli("-v", "helloworld")
    assert logging.getLogger().level == logging.DEBUG


def test_quiet_flag_sets_warning(run_cli: RunCli) -> None:
    run_cli("-q", "helloworld")
    assert logging.getLogger().level == logging.WARNING


def test_handler_renders_markdown() -> None:
    handler = MarkdownRichHandler()
    record = logging.LogRecord(
        name="test",
        level=logging.INFO,
        pathname="",
        lineno=0,
        msg="**bold**",
        args=None,
        exc_info=None,
    )
    assert isinstance(handler.render_message(record, "**bold**"), Markdown)
