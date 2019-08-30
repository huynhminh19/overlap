#!/bin/bash
# Apply database migrations
echo "Apply database migrations"
python manage.py makemigrations
python manage.py migrate
# Start test
echo "Starting test"
python manage.py test
