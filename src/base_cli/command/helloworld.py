from typing import Annotated

from typer import Option, echo

from base_cli.app import app


@app.command(help="Print a hello world greeting")
def helloworld(
    name: Annotated[str, Option(help="Name to greet")] = "world",
) -> None:
    echo(f"Hello, {name}!")
