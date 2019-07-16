"""
WSGI config for MeryPortfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os, sys
from django.core.wsgi import get_wsgi_application

path = '/MyPortfolioDjango/MeryPortfolio-project/MeryPortfolio/'
if path not in sys.path:
    sys.path.append(path)
while "." in sys.path:
    sys.path.remove(".")
while "" in sys.path:
    sys.path.remove("")

#('DJANGO_SETTINGS_MODULE', 'settings')
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MeryPortfolio.settings')
print(sys.path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.py'

application = get_wsgi_application()

# from MeryPortfolio.wsgi import MeryPortfolioApplication
# application = MeryPortfolioApplication(application)

