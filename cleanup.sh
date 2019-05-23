#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Shut down the docker container, if it exists
/usr/bin/docker ps -f 'ancestor=tensorflow/serving' -q | xargs -n1 /usr/bin/docker stop 2>/dev/null

# Remove the virtualenv
rm -rf "${DIR}/venv"
