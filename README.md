# Base CLI

Minimal CLI template with latest tooling and strict checks.

## Usage

```sh
$ uv run base-cli helloworld --name Alice
Hello, Alice!
```

## Development

```sh
make install # uv sync --locked
make check   # ruff, vulture, ty, pyright, mypy, pytest+coverage, yamllint
make upgrade # uv sync --upgrade
make clean   # remove caches
```
