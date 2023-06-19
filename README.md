# python-examples
This repository is to show python examples and explain them for learning purposes

## Prerequisites
In order to build the project using the `pyproject.toml` you need to install the `build` package.

```
python -m pip install --upgrade build
```

## Building
Building can be done with `python -m build` which will use your `pyproject.toml`.
A virtual environment will be created and the `[build-system]` section will be used to install the build requirements and then build the wheel and/or src distributions.

## Examples
### packaging-example
Shows how to setup a python project for building.

### unit-testing-example

