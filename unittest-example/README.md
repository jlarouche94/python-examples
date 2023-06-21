# unittest-example

## Prerequisites
This example will make use of `tox` for managing the unit test environments.
tox is a useful tool for testing a package in various python versions.
This is more important now that versions differences between python3 have quite some differences.

`pip install --upgrade tox`

## Core Components
### setup.py
setup.py is used by tox to know that there is a package to install. Also any additional values not supported by pyproject.toml will be placed here.
### pyproject.toml
### tox.ini
Tool for automating the process of testing.