#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# Load initial data only if database is empty (no categories exist)
python manage.py shell -c "
from shop.models import Category
if not Category.objects.exists():
    import subprocess
    result = subprocess.run(['python', 'manage.py', 'loaddata', 'datadump.json'], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
    print('Data loaded successfully!')
else:
    print('Database already has data, skipping loaddata.')
"
