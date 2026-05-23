#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Compile translation files (.po -> .mo)
python compile_messages.py

python manage.py collectstatic --no-input
python manage.py migrate
