from typing import Annotated

from typer import Option  # pyright: ignore[reportUnknownVariableType]

from base_cli.app import app


@app.command(help="Print a hello world greeting")
def helloworld(
    name: Annotated[str, Option(help="Name to greet")] = "world",
) -> None:
    print(f"Hello, {name}!")
