#!/usr/bin/env bash

VENVNAME=visual_venv

python3 -m venv $VENVNAME
source $VENVNAME/bin/activate
pip install --upgrade pip

test -f requirements.txt && pip install -r requirements.txt

echo "$VENVNAME built"