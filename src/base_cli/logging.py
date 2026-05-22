import logging

from rich.logging import RichHandler
from rich.markdown import Markdown


class MarkdownRichHandler(RichHandler):
    def render_message(self, record: logging.LogRecord, message: str) -> Markdown:
        return Markdown(message)


def configure_logging(verbosity: int = 0) -> None:
    """Set up root logging. `verbosity` is `-v` count minus `-q` count."""
    level = logging.INFO - verbosity * 10
    logging.basicConfig(
        level=level,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[MarkdownRichHandler()],
        force=True,
    )
    logging.getLogger("markdown_it").setLevel(logging.WARNING)
