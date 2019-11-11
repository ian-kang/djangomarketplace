"""
Django settings for icraig project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

"""
/***************************************************************************************
*  REFERENCES
*  Title: How to add Google and Github OAuth in Django
*  Author: Mohit
*  Date: Accessed 9/29/2019
*  Code version:
*  URL: https://fosstack.com/how-to-add-google-authentication-in-django/
*  Software License: none found
***************************************************************************************/
"""

import os
import django_heroku
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b5#!f2_vpg!-#db6fvtvodt-kn$(ctl9*x51!pgqz&!v!$*5&o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True 

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'craigslist.apps.CraigslistConfig',
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'social_django', #added for authentication
    'crispy_forms', #added to easily build, customize, and reuse forms
    'whitenoise.runserver_nostatic',
    'django_messages',
    'storages'
]
SITE_ID = 1

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware'
]

ROOT_URLCONF = 'icraig.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends', #added for authentication
                'social_django.context_processors.login_redirect',#added for authentication
            ],
        },
    },
]

WSGI_APPLICATION = 'icraig.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {}

# the following travis configuration was taken from https://gist.github.com/ndarville/3625246
if 'TRAVIS' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE':   'django.db.backends.postgresql_psycopg2',
            'NAME':     'travisci',
            'USER':     'postgres',
            'PASSWORD': '',
            'HOST':     'localhost',
            'PORT':     '',
        }
    }
else:
    DATABASES = {
        'default': {
            # 'ENGINE': 'django.db.backends.sqlite3',
            # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'dddj58uavbkv69',
            'USER': 'bkpfdxenqgaqph',
            'PASSWORD': '3d58641687f1f6dec1284e7c69638a487b74c8d7ca6c7ce2b9b7c11c74c5dac2',
            'HOST': 'ec2-107-21-120-104.compute-1.amazonaws.com',
            'PORT': '5432',
            #Previous
            #'ENGINE': 'django.db.backends.postgresql',
            #'NAME': 'listings',
            #'USER': 'postgres',
            #'PASSWORD': 'password',
            #'HOST': 'localhost',
            #'PORT': '',

        }
    }

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

AUTHENTICATION_BACKENDS = (
 'social_core.backends.open_id.OpenIdAuth',  # for Google authentication
 'social_core.backends.google.GoogleOpenId',  # for Google authentication
 'social_core.backends.google.GoogleOAuth2',  # for Google authentication
 
 'django.contrib.auth.backends.ModelBackend',
)

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
django_heroku.settings(locals())

django_heroku.settings(locals())

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '200446462519-9nrggfc8md7q62k485tbsiikbm6ds465.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'N8zOCeL-kNMss9rgwhYS6iuG'
SOCIAL_AUTH_GOOGLE_OAUTH2_WHITELISTED_DOMAINS = ['virginia.edu']
SOCIAL_AUTH_LOGIN_ERROR_URL = '/accounts/login/'
SOCIAL_AUTH_BACKEND_ERROR_URL = '/accounts/login/'

LOGIN_URL = '/auth/login/google-oauth2/'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
AWS_ACCESS_KEY_ID = 'AKIAXDVC2B5TQ5N5T53N'
AWS_SECRET_ACCESS_KEY = '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'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_STORAGE_BUCKET_NAME = 'icraig'
AWS_S3_REGION_NAME = 'us-east-1'
AWS_S3_CUSTOM_DOMAIN = 'icraig.s3.amazonaws.com'
DEFAULT_FILE_STORAGE = 'icraig.storage_backends.MediaStorage'
#MEDIA_ROOT =  os.path.join(BASE_DIR, 'media') 
#MEDIA_URL = '/media/'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
