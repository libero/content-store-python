#!/bin/sh

set -e

# avoid issues with .pyc/pyo files when mounting source directory
export PYTHONOPTIMIZE=

pytest
pylint content_store tests
flake8 content_store tests
