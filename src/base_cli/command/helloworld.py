import logging

logger = logging.getLogger(__name__)


def run(name: str) -> int:
    logger.debug("Preparing greeting for %s", name)
    print(f"Hello, {name}!")
    return 0
