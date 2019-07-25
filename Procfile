release: python portfolioproject//manage.py migrate
web: gunicorn portfolioproject.meryportfolio.wsgi:jobs --preload --workers=1 --log-file - --log-level debug
