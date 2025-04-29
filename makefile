.PHONY: changelog start venv setup help
.SILENT:

help: ## | List all available commands
	echo "Available commands in this makefile"
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
	| sed -n 's/^\(.*\): \(.*\)##\(.*\)/\1\3/p' \
	| column -t -s '|'

venv: ## | create a virtual environment
	echo "Creating virtual environment..."
	uv venv
	echo "Environment created. Run the following command before continuing:"
	echo
	echo "source .venv/bin/activate"
	echo
	echo

setup: ## | Install dependencies and perform any initial setup actions
	echo "Installing dependencies with uv..."
	uv pip install -r pyproject.toml


ARGS=

start: ## | Start the (dev or production) server (convenience).
	fastapi dev $(ARGS)


upgrade: ## | Upgrade ALL project dependencies at once
	uv lock --upgrade
