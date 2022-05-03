"""
Django settings for gpa10 project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/

REFERENCES
  Title: Django Google Authentication using django-allauth
  Author: Muhd Rahiman
  Date: 3/14/2022
  URL: https://dev.to/mdrhmn/django-google-authentication-using-django-allauth-18f8

  Title: How to use Google Cloud Storage with Django Application
  Author: Mohammed Abuiriban
  URL: https://medium.com/@mohammedabuiriban/how-to-use-google-cloud-storage-with-django-application-ff698f5a740f

  Title: <title of program/source code>
  Author: <author(s) names>
  Date: <date>
  Code version: <code version>
  URL: <where it's located>
  Software License: <license software is released under>

  Title: <title of program/source code>
  Author: <author(s) names>
  Date: <date>
  Code version: <code version>
  URL: <where it's located>
  Software License: <license software is released under>

  Title: <title of program/source code>
  Author: <author(s) names>
  Date: <date>
  Code version: <code version>
  URL: <where it's located>
  Software License: <license software is released under>

"""
import sys
from pathlib import Path
from google.oauth2 import service_account
# import django_heroku

import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ***REMOVED***

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'https://group-project-a-10.herokuapp.com/',
    '0.0.0.0',
    '127.0.0.1',
    '*',
]

# Application definition

INSTALLED_APPS = [
    'wordofmouth.apps.WordofmouthConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # added for google login
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    #
    'social_django',
    'taggit',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gpa10.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'wordofmouth/templates/wordofmouth'),], #used to be templates/ didnt work for add_comment
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'gpa10.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': ***REMOVED***
        'USER': ***REMOVED***,
        'PASSWORD': ***REMOVED***,
        'HOST': ***REMOVED***,
        'PORT': ***REMOVED***,
    }
}


# if 'HEROKU' in os.environ:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql_psycopg2',
#             'NAME': ***REMOVED***
#             'USER': ***REMOVED***,
#             'PASSWORD': ***REMOVED***,
#             'HOST': ***REMOVED***,
#             'PORT': ***REMOVED***,
#         }
#     }
# else:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': BASE_DIR / 'db.sqlite3',
#         }
#     }

# if 'test' in sys.argv:  # testing database

# else:  # regular database
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql_psycopg2',
#             'NAME': ***REMOVED***
#             'USER': ***REMOVED***,
#             'PASSWORD': ***REMOVED***,
#             'HOST': ***REMOVED***,
#             'PORT': ***REMOVED***,
#         }
#     }


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# django_heroku.settings(locals())

# added lines below for google login
# FIXME: I don't think these static files are going to show
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
                os.path.join(BASE_DIR,'wordofmouth/static/'), # if your static files folder is named "staticfiles"
)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.google.GoogleOAuth2',
    'allauth.account.auth_backends.AuthenticationBackend'
]

SITE_ID = 2
LOGIN_REDIRECT_URL = '/'

# Additional configuration settings
# followed this tutorial: https://dev.to/mdrhmn/django-google-authentication-using-django-allauth-18f8
SOCIALACCOUNT_QUERY_EMAIL = True
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_REQUIRED = True

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

try:
    if 'HEROKU' in os.environ:
        import django_heroku

        django_heroku.settings(locals())
except ImportError:
    found = False

# storage
GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
    os.path.join(BASE_DIR, 'word-of-mouth-345423-bd82fc5e675d.json')
)
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_BUCKET_NAME = 'a10-word-of-mouth'
STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

SOCIALACCOUNT_LOGIN_ON_GET=True