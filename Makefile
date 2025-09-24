.PHONY: help install dev-install format lint test clean

help:
	@echo "Common targets:"
	@echo "  make dev-install   # Install package with dev tools"
	@echo "  make format        # Auto-format with ruff+black"
	@echo "  make lint          # Lint with ruff"
	@echo "  make test          # Run pytest"
	@echo "  make clean         # Remove caches and build artifacts"

install:
	pip install -e .

dev-install:
	pip install -e .[dev]
	pre-commit install || true

format:
	ruff format .
	black .
	ruff check --fix .

lint:
	ruff check .
	black --check .

test:
	pytest -q

clean:
	rm -rf build/ dist/ *.egg-info .pytest_cache .ruff_cache .mypy_cache .nox .tox htmlcov
	find . -name "__pycache__" -type d -prune -exec rm -rf {} +

