#!/bin/bash

# Apply database migrations
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input

# Define environment variables
export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_PASSWORD=admin
export DJANGO_SUPERUSER_EMAIL=admin@example.com

# Create superuser
python manage.py createsuperuser --no-input

# Run the Django development server
python manage.py runserver 0.0.0.0:8000
