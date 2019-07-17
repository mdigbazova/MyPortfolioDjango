from . import base
import django_heroku

# Other settings required only for live server
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qnds&b(vyfz_tk2w!(oyq-&^!-8b_hw%i!*8ohfchj1ftw7a&m'

ALLOWED_HOSTS = ['shielded-ocean-74848.herokuapp.com']

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # 'django.db.backends.sqlite3'
        'NAME': 'd1kq5er2d310b9',
        'USER': 'rhpzbalsaqtahy',
        'PASSWORD': '2b6a00a5eca2db664e49c75a94efaf34ce3446cc59654e865975e98f74b1f6a0',
        'HOST': 'ec2-50-19-222-129.compute-1.amazonaws.com',
        'PORT': '5432'
    }
}



# Configure Django App for Heroku.
#import django_heroku
django_heroku.settings(locals())
