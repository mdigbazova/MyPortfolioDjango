release: python meryportfolio-project/manage.py migrate
web: gunicorn meryportfolio-project.meryportfolio.wsgi:jobs --preload --workers=1 --log-file - --log-level debug
