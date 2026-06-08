from base_cli.app import app
from base_cli.command.goodbye import goodbye
from base_cli.command.helloworld import helloworld

__all__ = ["app", "goodbye", "helloworld"]

if __name__ == "__main__":
    app()  # pragma: no cover
