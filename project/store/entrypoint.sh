#!/bin/bash
set -e

if [ ! -f store.db ]; then
    echo "No database found — seeding..."
    python manage.py
fi

exec python app.py
