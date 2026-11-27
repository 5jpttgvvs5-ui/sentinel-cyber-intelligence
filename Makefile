install:
	pip install -e ".[dev]"

run:
	uvicorn sentinel.main:app --reload --app-dir src

test:
	pytest

lint:
	ruff check .

check: lint test
