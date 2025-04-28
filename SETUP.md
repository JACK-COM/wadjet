# Set up UV

The following instructions should prepare you to get started with this project for the first time. You only need to performe them once.

At a high level, you will need to take these steps:

1. Install `uv` globally for working with [dependencies](./README.md#dependencies).

Once you have your database and `.env` file configured, and have installed `uv`, you can continue with the steps below.

The first two steps can be performed in any order, since they are independent of each other.

## Table of Contents

- [Set up UV](#set-up-uv)
  - [Table of Contents](#table-of-contents)
  - [1. Install uv](#1-install-uv)
  - [2. Create a virtual environment target for dependencies](#2-create-a-virtual-environment-target-for-dependencies)
    - [(OPTIONAL) Activate your virtual environment in VSCode](#optional-activate-your-virtual-environment-in-vscode)
  - [3. Add dependencies](#3-add-dependencies)

## 1. Install uv

> `uv` installation docs [here](https://docs.astral.sh/uv/getting-started/installation/).

Install [`uv`](https://docs.astral.sh/uv/) globally if you don't already have it installed. If you don't have Python installed, `uv` can help with that too. Just visit their installation docs link for instructions that suit your platform (Windows/Linux/macOS).

## 2. Create a virtual environment target for dependencies

If you have `make` installed, create a new virtual environment for `uv`'s dependencies:

```bash
# 1. Create a virtual environment (makefile installed)
$. make venv # (or, without makefile, "uv venv")

# 2. Activate the virtual environment:
$. source .venv/bin/activate
```

### (OPTIONAL) Activate your virtual environment in VSCode

If you use **VSCode** for development, creating a virtual environment now triggers the code editor to ask if you want to switch to it. Confirm the prompt to switch to the new v-env.\
If you don't receive a prompt or are using a separate/standalone terminal for setup, follow these steps in VSCode to ensure new dependencies are installed to the right environment.

1. Open your **Commands** menu (mac: `cmd + shift + P`; windows: `ctrl + shift + p`).
2. Search for **Python: Select Interpreter** and click on it to open a venv target dropdown.
3. In the target dropdown, select the `./.venv/bin/python` environment.

And now you're MOAR REDDY to get started.

## 3. Add dependencies

If you have `make` installed, you can use the following convenience command:

```bash
# Install dependencies
make add-deps  # (or, without makefile, "uv pip install -r pyproject.toml") 
```
