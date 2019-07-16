"""
WSGI config for MeryPortfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os


from django.core.wsgi import get_wsgi_application
from . import settings as settingsfile

#('DJANGO_SETTINGS_MODULE', 'settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settingsfile')
#os.environ["DJANGO_SETTINGS_MODULE"] = "meryportfolio.settings"

application = get_wsgi_application()

# from MeryPortfolio.wsgi import MeryPortfolioApplication
# application = MeryPortfolioApplication(application)

