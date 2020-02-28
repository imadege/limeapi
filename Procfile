release: python manage.py makemigrations  && pythom manage.py migrate

web: gunicorn config.wsgi:application