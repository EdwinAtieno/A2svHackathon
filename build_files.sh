#!/usr/bin/env bash

echo "Building project packages..."
pip install -r requirements.txt

echo "Migrating Database..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting the application..."
gunicorn a2svhackathon.wsgi --bind 0.0.0.0:$PORT
