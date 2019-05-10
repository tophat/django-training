#!/usr/bin/env bash

PORT=8000

# Run migrations
python manage.py migrate
# Load the database with fixtures
python manage.py loaddata users

python manage.py runserver ${PORT}
