release: python MeryPortfolio-project//manage.py migrate
web: gunicorn MeryPortfolio.wsgi:jobs --preload --workers=1 --debug --log-level debug
