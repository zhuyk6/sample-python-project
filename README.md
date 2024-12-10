# Sample-Python-Project

## Test

Using [`pytest`](https://docs.pytest.org/en/stable/index.html).

[Reference](https://docs.pytest.org/en/stable/explanation/goodpractices.html).


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