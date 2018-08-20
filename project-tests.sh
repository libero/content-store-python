#!/bin/sh

set -e

export PYTHONOPTIMIZE=

pytest && \
    pylint content_store tests
