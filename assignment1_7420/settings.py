"""
Django settings for assignment1_7420 project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import django_heroku



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!zvxsu$ak85ou&gu7&6w@qg+h)mc%22)d(bs@23=a6ixaaolo5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'http://127.0.0.1:8000/',
    'localhost',
    'djangoeventattendee.herokuapp.com',
    'djangoevents.live'
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'events.apps.EventsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',

]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'assignment1_7420.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'assignment1_7420.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Events',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': '127.0.0.1',
        'PORT': '5432',

    }  ,

#PostgreSQL on Heroku via Amazon AWS

    # 'default': {
    #
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'd4u0ete0bfnv17',
    #     'USER': 'kdtvmrjgqazhvw',
    #     'PASSWORD': '5965efc227cbc84f1e3f9eff040455e2286d33447700c05f05ebb3c594891676',
    #     'HOST': 'ec2-34-230-149-169.compute-1.amazonaws.com',
    #     'PORT': '5432',
    # }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# Loading Static images from Amazon S3 Bucket

#   AWS Access Keys

AWS_ACCESS_KEY_ID = 'AKIAJAZXKTY7K3DENXEA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'django-events-images'
AWS_S3_REGION_NAME = 'ap-southeast-2'
AWS_S3_ENDPOINT_URL = 'https://s3-ap-southeast-2.amazonaws.com'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#AWS_LOCATION = ''
#AWS_S3_ADDRESSING_STYLE = ''



# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

 # Media Folder Settings

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'



django_heroku.settings(locals())
