#!/bin/sh

set -e

docker run --rm -v $(pwd):/data gouvinb/docker-markdownlint \
    --config .markdownlint \
    *.md
