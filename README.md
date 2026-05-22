# Base CLI

[![ci](https://github.com/robecclin/base-cli-py/actions/workflows/ci.yml/badge.svg)](https://github.com/robecclin/base-cli-py/actions/workflows/ci.yml)

Minimal bleeding-edge Python CLI template with latest tooling, strict
type checking, linting, formatting, and 100% coverage.

## Usage

```sh
$ uv run base-cli helloworld --name Alice
Hello, Alice!
```

## Fork

1. Click **Use this template** on GitHub (or `gh repo create --template`).
2. Rename the package: change `base-cli` → `your-cli` and `base_cli` →
   `your_cli` in `pyproject.toml`, `src/`, and `tests/`.
3. Update `description`, the CI badge URL, and `LICENSE` copyright.
4. `make install && make check`.

## Development

```sh
make install   # uv sync --locked
make check     # ruff, vulture, ty, pyright, mypy, pytest+coverage, yamllint
make upgrade   # uv sync --upgrade
make clean     # remove caches
```

### Layout

```
src/base_cli/
  app.py             # typer app instance
  main.py            # entry point: wires app + commands
  command/           # one module per subcommand
tests/               # pytest suite (100% coverage required)
```

### Add a subcommand

1. Create `src/base_cli/command/foo.py` with a `@app.command(...)` function.
2. Import it in `main.py` so it registers on the app.
3. Add a test in `tests/test_main.py`.
4. `make check` (must stay at 100% coverage).

## License

Apache 2.0 — see [LICENSE](LICENSE).
