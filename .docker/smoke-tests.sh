#!/bin/bash
set -e

timeout=30

curl_command="curl -sS localhost:5000/articles/ping | grep pong"
echo "Requesting /articles/ping..."
timeout "$timeout" bash -c "
    while : ; do
        echo 'Attempt...'
        ${curl_command} && break || echo ping failed
        sleep 1
        echo
    done
"
