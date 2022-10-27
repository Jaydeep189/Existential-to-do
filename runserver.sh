#!/bin/sh

python manage.py collectstatic --no-input
python manage.py migrate
gunicorn existential.wsgi --bind=0.0.0.0:80