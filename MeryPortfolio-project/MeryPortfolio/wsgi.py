"""
WSGI config for MeryPortfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os


from django.core.wsgi import get_wsgi_application

#('DJANGO_SETTINGS_MODULE', 'settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meryportfolio.settings')
#os.environ["DJANGO_SETTINGS_MODULE"] = "meryportfolio.settings"

application = get_wsgi_application()

