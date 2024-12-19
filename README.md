# Sample-Python-Project

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/zhuyk6/sample-python-project/.github%2Fworkflows%2Fci.yml?logo=github&label=ci)
![GitHub License](https://img.shields.io/github/license/zhuyk6/sample-python-project)
![Code Coverage](./assets/coverage-badge.svg)
[![Docs](https://img.shields.io/badge/docs-blue)](https://zhuyk6.github.io/sample-python-project/)

## Usage

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

- Document: [`pdoc`](https://pdoc.dev/)

## Notes

### `PYTHONPATH` environment variable

The following problem is because Python can't find your module under `src/`.
```shell
(sample-python-project) zhuyk6@zbook-arch ~/t/sample-python-project (dev)> uv run tests/test_fib.py
Traceback (most recent call last):
  File "/home/zhuyk6/test/sample-python-project/tests/test_fib.py", line 2, in <module>
    from mypkg.fib import fib  # type: ignore
    ^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'mypkg'
```

This variable is to help adding directories to Python module search path.
After setting `PYTHONPATH=$pwd/src`, you can run the scripts out of `src/` folder, such as `tests/test_fib.py`.

- For Linux user, you can just `export PYTHONPATH=$(pwd)/src` at the root of the project.
- For Windows, 
    - CMD: `set PYTHONPATH=%CD%\src`
    - PowerShell: `$env:PYTHONPATH = $PWD.Path + "\src"`

I have added this environment variable into `.env` file. `uv run` support load environment variables from dotenv files.
You can just run `uv run --env-file .env tests/test_fib.py`.

> In fact in this project, there is no need to run python file in `tests/` folder seperately.
> 
> You just need `pytest` to run tests under `tests/` folder, since I have added configurations for `pytest` in `pyproject.toml`.