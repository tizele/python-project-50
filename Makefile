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
	uv run ruff check

lint-fix: #code check fix
	uv run ruff check --fix
