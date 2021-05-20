#!/usr/bin/env bash

VENVNAME=venv

python3 -m venv $VENVNAME
source $VENVNAME/bin/activate
pip install --upgrade pip

test -f requirements.txt && pip install -r requirements.txt

mkdir assignment_3/data

echo "$VENVNAME built"