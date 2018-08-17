#!/bin/bash
set -e

timeout=30

curl_command="curl -sS localhost:5000/ping | grep pong"
echo "ping..."
timeout "$timeout" bash -c "while ! ${curl_command}; do sleep 1; done"
