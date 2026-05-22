import logging
from typing import Annotated

from rich import print
from typer import Option  # pyright: ignore[reportUnknownVariableType]

from base_cli.app import app

logger = logging.getLogger(__name__)


@app.command(help="Print a hello world greeting")
def helloworld(
    name: Annotated[str, Option(help="Name to greet")] = "world",
) -> None:
    logger.debug("Preparing greeting for %s", name)
    print(f"Hello, {name}!")
