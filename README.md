# Wadjet 🐍

A python-Langchain-FastAPI project starter. See [dependencies](#dependencies) for the list, as well as documentation links.\
At a high-level, it provides the following dependencies:

1. `UV` for project management
2. LangChain (python) -- comes with
   1. LangGraph
   2. LangGraph-Checkpoint-SQLite
   3. LangchainAnthropic
   4. LangchainCommunity
3. FastAPI
4. Python-dotenv (for `.env` files)

You can remove or add any dependencies you need.\
If you are familiar with any of the [dependencies](#dependencies) and/or Python, the template should be straightforward to use.

## Table of Contents

- [Wadjet 🐍](#wadjet-)
  - [Table of Contents](#table-of-contents)
  - [Development](#development)
    - [1. Initial Setup](#1-initial-setup)
    - [2. Run the project](#2-run-the-project)
      - [Development Environment](#development-environment)
      - [Start API Server](#start-api-server)
        - [Override Default Port](#override-default-port)
  - [Dependencies](#dependencies)
    - [What is uv?](#what-is-uv)
    - [Dependency management with uv](#dependency-management-with-uv)
    - [Additional uv scripts](#additional-uv-scripts)
  - [Troubleshooting](#troubleshooting)
    - [Resolve dependency paths in VSCode](#resolve-dependency-paths-in-vscode)

## Development

### 1. Initial Setup

Follow the steps outlined [**here**](./SETUP.md) to set up your dev environment.

### 2. Run the project

#### Development Environment

#### Start API Server

Any of the following commands will start the server.

```bash
# (RECOMMENDED) call fastapi (defaults to port 8000)
$. make start  # (or "fastapi dev")

# (ALTERNATIVE) call fastapi directly. Include additional options 
# to override port, host, or entry file:
#
# $. fastapi dev [ custom_entry_file.py --port 1234 ]
```

##### Override Default Port

Use the optional `ARGS` string to pass any additional flags to `fastapi[standard]`:

```bash
# (EXAMPLE) run on custom port (1234 in this case)
$. make start ARGS="--port 1234" # == "fastapi dev --port 1234"

# (EXAMPLE) run a custom entry file
$. make start ARGS="entry_file.py" # == "fastapi dev entry_file.py
```

See [additional scripts](#additional-uv-scripts) for commands to update one or more dependencies.

## Dependencies

Documentation links are provided for each dependency.

- [`uv`](https://docs.astral.sh/uv/): dependency and project manager.
- [GNU `make`](https://www.gnu.org/software/make/manual/make.html): For running `makefiles`. Should already be installed in your system. Highly recommended.
- [`python-dotenv`](https://pypi.org/project/python-dotenv/): for reading `.env` files in project
- [`langchain` (python)](https://python.langchain.com/docs/introduction/): for integrating LLM APIs
- [`fastapi[standard]`](https://fastapi.tiangolo.com/): a high performance API framework.

### What is uv?

[`uv`](https://docs.astral.sh/uv/) is a project and dependency manager. If you are familiar with NodeJS, it is somewhat similar to `npm`, in that you can use it to

- Initialize a project in a directory
- Install, review, and update project dependencies
- Create a dependency `.lock` file that freezes your dependency versions

### Dependency management with uv

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
