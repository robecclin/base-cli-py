from .app import app
from .command.goodbye import goodbye  # pyright: ignore[reportUnusedImport]  # noqa: F401
from .command.helloworld import helloworld  # pyright: ignore[reportUnusedImport]  # noqa: F401
from .logging import configure_logging

configure_logging()

if __name__ == "__main__":
    app()  # pragma: no cover
