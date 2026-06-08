from typing import Annotated

from typer import Option  # pyright: ignore[reportUnknownVariableType]

from base_cli.app import app


@app.command(help="Print a goodbye farewell")
def goodbye(
    name: Annotated[str, Option(help="Name to bid farewell")] = "world",
) -> None:
    print(f"Goodbye, {name}!")
