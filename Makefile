install: #install package
	uv sync

reinstall: #start
	uv sync
	uv build
	uv tool install --force dist/*.whl

build: #assembly
	uv build

package-install:
	uv tool install dist/*.whl

package-force:
	uv tool install --force dist/*.whl

lint: #code check
	uv run ruff check gendiff

lint-fix: #code check fix
	uv run ruff check --fix

test: 
	uv run pytest

check: 
	test lint

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml:converage.xml
