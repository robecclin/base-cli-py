import logging

from rich.logging import RichHandler
from rich.markdown import Markdown


class MarkdownRichHandler(RichHandler):
    def render_message(self, record: logging.LogRecord, message: str) -> Markdown:
        return Markdown(message)


def configure_logging() -> None:
    """Set up root logging."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[MarkdownRichHandler()],
        force=True,
    )
