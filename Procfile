release: python manage.py migrate
web: gunicorn core.wsgi -t 180 --preload -w 4 --log-file -
