## packages

django
python-dotenv
djangorestframework
pytest
pytest-django

## commands

- django-admin startproject (project-name)
- py manage.py runserver

## Generate NEW SECRET_KEY
- from django.core.management.utils import get_random_secret_key
- print(get_random_secret_key())