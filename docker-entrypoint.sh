#!/bin/bash

# Apply database migrations
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input


# Other initialization tasks (e.g., collect static files, create superuser, etc.)
# Add them here as needed

# Run the Django development server
# python manage.py runserver 0.0.0.0:8000
