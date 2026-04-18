.PHONY: check clean

check:
	uv run ruff check
	uv run ruff format --check
	uv run ty check
	uv run pyright
	uv run mypy
	uv run coverage run -m pytest
	uv run coverage report

clean:
	rm -rf .coverage .pytest_cache .ruff_cache .mypy_cache
	find . -type d -name __pycache__ -exec rm -rf {} +
