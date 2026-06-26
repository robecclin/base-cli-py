from typing import Annotated

from typer import Option, echo

from base_cli.app import app


@app.command(help="Print a goodbye farewell")
def goodbye(
    name: Annotated[str, Option(help="Name to bid farewell")] = "world",
) -> None:
    echo(f"Goodbye, {name}!")
