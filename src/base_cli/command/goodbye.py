import logging
from typing import Annotated

from typer import Option  # pyright: ignore[reportUnknownVariableType]

from base_cli.app import app

logger = logging.getLogger(__name__)


@app.command(help="Print a goodbye farewell")
def goodbye(
    name: Annotated[str, Option(help="Name to bid farewell")] = "world",
) -> None:
    logger.info("Preparing farewell for %s", name)
    print(f"Goodbye, {name}!")
