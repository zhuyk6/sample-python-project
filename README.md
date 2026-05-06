# Sample-Python-Project

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/zhuyk6/sample-python-project/.github%2Fworkflows%2Fci.yml?logo=github&label=ci)
![GitHub License](https://img.shields.io/github/license/zhuyk6/sample-python-project)
![Code Coverage](./assets/coverage-badge.svg)

## Usage

- Init: use `uv sync` to create `.venv` and install dependencies.

- Just use `uv run`:

    This will create a virtual python environment (or `uv sync` explicitly)

- You can also activate the virtual environment.
  1. Install all dependencies: `uv sync`
  2. Load the virtual environment (under `.venv`):

      Under `.venv\bin` there are several scripts to activate venv. 
      - Fish shell: `source .venv/bin/activate.fish`
      - PowerShell: `.\.venv\bin\activate.ps1`
      - CMD: `.\.venv\bin\activate.bat`

  3. Use whatever you want: `python` or `pytest`.


## Tools

- Package and project manager: [`uv`](https://docs.astral.sh/uv/)

- Test: [`pytest`](https://docs.pytest.org/en/stable/index.html), here is a [reference](https://docs.pytest.org/en/stable/explanation/goodpractices.html).

- Format: [`ruff`](https://docs.astral.sh/ruff/formatter/) 
