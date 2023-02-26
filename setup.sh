#!/usr/bin/env bash

# exit on error
set -o errexit

## Install Dependencies
pip install -r dependencies.txt

# run migrations
python manage.py migrate