#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

/usr/bin/tar -xvf "${DIR}/Resources.tar.gz"

/usr/bin/python3 -m virtualenv "${DIR}/venv"
source "${DIR}/venv/bin/activate"
pip install --upgrade pip
pip install -r requirements.txt

jupyter notebook
