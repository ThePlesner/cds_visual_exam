#!/usr/bin/env bash

VENVNAME=visual_venv

python -m venv $VENVNAME
source $VENVNAME/scripts/activate
pip install --upgrade pip

test -f requirements.txt && pip install -r requirements.txt

echo "$VENVNAME built"