# Base CLI

[![ci](https://github.com/robecclin/base-cli-py/actions/workflows/ci.yml/badge.svg)](https://github.com/robecclin/base-cli-py/actions/workflows/ci.yml)

Minimal Python CLI template with strict type checking, linting,
formatting, and 100% coverage.

## Usage

```sh
$ uv run base-cli helloworld --name Alice
Hello, Alice!
```

## Development

```sh
make install   # uv sync --locked
make check     # ruff, vulture, ty, pyright, mypy, pytest+coverage, yamllint
make upgrade   # uv sync --upgrade
make clean     # remove caches
```

## Layout

```
src/base_cli/
  main.py            # argparse entry point
  command/           # one module per subcommand
tests/               # pytest suite (100% coverage required)
```

## License

Apache 2.0 — see [LICENSE](LICENSE).
