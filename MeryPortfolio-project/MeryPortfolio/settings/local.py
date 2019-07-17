from . import base

# Other settings required only for local server like
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qnds&b(vyfz_tk2w!(oyq-&^!-8b_hw%i!*8ohfchj1ftw7a&m'

ALLOWED_HOSTS = []

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # 'django.db.backends.sqlite3'
        'NAME': 'portfoliodb',
        'USER': 'postgres',
        'PASSWORD':'SitePortfolio',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}