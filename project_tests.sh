#!/bin/sh

set -e

pytest && \
    pylint content_store/api/*.py