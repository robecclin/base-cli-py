import argparse
import sys

from base_cli_py.command import helloworld


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="base-cli-py", description="Base CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    hello = subparsers.add_parser("helloworld", help="Print a hello world greeting")
    hello.add_argument("--name", default="world", help="Name to greet")

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    match args.command:
        case "helloworld":
            return helloworld.run(args.name)
        case _:  # pragma: no cover
            raise AssertionError(f"unreachable: unknown command {args.command!r}")


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
