# Wadjet

A python-LLM REST API project starter. See [dependencies](#dependencies) for the list, as well as documentation links. At a high-level, it suggests or provides the following dependencies:

1. UV for project management
2. LangChain (python)
3. FastAPI
4. Python-dotenv (for `.env` files)

If you are familiar with any of the [dependencies](#dependencies) and/or Python, it should be straightforward to use.

## Table of Contents

- [Wadjet](#wadjet)
  - [Table of Contents](#table-of-contents)
  - [Development](#development)
    - [1. Initial Setup](#1-initial-setup)
    - [2. Run the project](#2-run-the-project)
      - [Development Environment](#development-environment)
      - [Start API Server](#start-api-server)
  - [Dependencies](#dependencies)
    - [What is uv?](#what-is-uv)
    - [Adding dependencies with uv](#adding-dependencies-with-uv)
    - [Additional uv scripts](#additional-uv-scripts)
  - [Troubleshooting](#troubleshooting)
    - [Resolve dependency paths in VSCode](#resolve-dependency-paths-in-vscode)

## Development

### 1. Initial Setup

Follow the steps outlined [**here**](./SETUP.md) to set up your dev environment.

### 2. Run the project

#### Development Environment

Run the following in the project root (where `pyproject.toml` can be found).\
This will run the application in dev mode on port `8000`.

If you have `make` installed, you can use the following convenience command:

```bash
$. make start # (or, without make, "uv run dev.py")
```

See [additional scripts](#additional-uv-scripts) for commands to update one or more dependencies.

#### Start API Server

Any of the following commands will start the server.

```bash
# call fastapi 
$. make start 

# Without `make` installed, use ANY of the following:

# 1. (PREFERRED) start fastapi with uv (used by "make start" above)
# > uv run fastapi dev main.py

# 2. (ALTERNATIVE) start SPECIFIC entry file:
# > fastapi dev main.py

# 3. (ALTERNATIVE) start DEFAULT entry file (assumes "main.py")
# > fastapi dev
```

## Dependencies

Documentation links are provided for each dependency.

- [`uv`](https://docs.astral.sh/uv/): dependency and project manager.
- [GNU `make`](https://www.gnu.org/software/make/manual/make.html): For running `makefiles`. Should already be installed in your system.
- [`python-dotenv`](https://pypi.org/project/python-dotenv/): for reading `.env` files in project
- [`langchain` (python)](https://python.langchain.com/docs/introduction/): for integrating LLM APIs
- [`fastapi`](https://fastapi.tiangolo.com/): a high performance API framework.

### What is uv?

[`uv`](https://docs.astral.sh/uv/) is a project and dependency manager. If you are familiar with NodeJS, it is somewhat similar to `npm`, in that you can use it to

- Initialize a project in a directory
- Install, review, and update project dependencies
- Create a dependency `.lock` file that freezes your dependency versions

### Adding dependencies with uv

You can use the following scripts to add, remove, or manage your dependencies:

- `uv add [dependency] [dependency] ...`: install new package(s) and update `project.toml`
- `uv remove [dependency]`: uninstall package
- `uv lock --upgrade`: **upgrade all packages** listed in `project.toml`
- `uv lock --upgrade [dependency]`: **upgrade a specified dependency** listed in `project.toml`

### Additional uv scripts

The following additional scripts help you run the project

- `uv run fastapi dev main.py`: run project
- `uv run [script]`: run any script in project context
- `uv build`: build a project bundle for distribution

## Troubleshooting

### Resolve dependency paths in VSCode

Worth noting, since I personally ran into this issue: if you are using VSCode, be sure to

- Open your command menu (**ctrl (or cmd for mac) + shift + p**),
- Search for and select the `Python: Select Interpreter` command, then
- Make sure it points to the virtual environment in the current directory (path begins with `.venv/...`)

This will ensure your workspace can correctly resolve dependencies.
