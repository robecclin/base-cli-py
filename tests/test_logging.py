import logging

from rich.markdown import Markdown

from base_cli.logging import MarkdownRichHandler, configure_logging


def test_default_level_is_info() -> None:
    configure_logging()
    assert logging.getLogger().level == logging.INFO


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
