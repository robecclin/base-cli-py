from base_cli.app import app
from base_cli.command.goodbye import goodbye
from base_cli.command.helloworld import helloworld
from base_cli.logging import configure_logging

__all__ = ["app", "goodbye", "helloworld"]

configure_logging()

if __name__ == "__main__":
    app()  # pragma: no cover
