'''
    FILE FOR DEVELOPMENT 
'''

from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ocu0mqd9kytw&!0h11^%!rqx%0j6y9(pp%$x-s)v*u^pmn%5$%'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront3',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'sukhmeet306singh',
    }
}
