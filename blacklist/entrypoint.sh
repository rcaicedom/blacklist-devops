#!/bin/bash
if $TEST_COVERAGE; then
    poetry run python src/database/exec_create_all.py
    poetry run coverage run -m pytest
    poetry run coverage report --fail-under=70
else
    #!poetry run python src/database/exec_create_all.py
    poetry run python src/app.py
fi