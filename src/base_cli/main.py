import argparse
import sys
from importlib.metadata import version

from base_cli.command import helloworld
from base_cli.logging import configure_logging


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="base-cli", description="Base CLI")
    parser.add_argument("--version", action="version", version=f"%(prog)s {version('base-cli')}")
    parser.add_argument("-v", "--verbose", action="count", default=0, help="Increase verbosity")
    parser.add_argument("-q", "--quiet", action="count", default=0, help="Decrease verbosity")
    subparsers = parser.add_subparsers(dest="command", required=True)

    hello = subparsers.add_parser("helloworld", help="Print a hello world greeting")
    hello.add_argument("--name", default="world", help="Name to greet")

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    configure_logging(verbosity=args.verbose - args.quiet)
    match args.command:
        case "helloworld":
            return helloworld.run(args.name)
        case _:  # pragma: no cover
            raise AssertionError(f"unreachable: unknown command {args.command!r}")


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
