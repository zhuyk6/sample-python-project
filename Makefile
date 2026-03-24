.DEFAULT_GOAL := help

.PHONY: help hooks format lint test test-cov

help:
	@echo "Targets:"
	@echo "  make format  - Fix import order + format code (ruff)"
	@echo "  make lint    - Lint + format check (ruff)"
	@echo "  make test    - Run tests (pytest)"
	@echo "  make test-cov - Run tests with coverage (writes cov.xml)"
	@echo "  make hooks   - Install git pre-commit hook"

hooks:
	uv run pre-commit install

format:
	uv run ruff check . --select I --fix
	uv run ruff format

lint:
	uv run ruff check .
	uv run ruff format --check

test:
	uv run pytest

test-cov:
	uv run pytest --cov=src --cov-report=term-missing --cov-report=xml:cov.xml
