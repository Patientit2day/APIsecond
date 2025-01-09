"""
Django settings for FluxyApi project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1i19#-hdjmo+xwogmrujduzt-akm^a1fhx%g*j^m8mh=d_$8i1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'rest_framework_simplejwt',
    'Api',
    'silk',
    'django_elasticsearch_dsl',
    'django_elasticsearch_dsl_drf',
    'channels',
   
]
ASGI_APPLICATION = "FluxyApi.asgi.application"
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'silk.middleware.SilkyMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication',)
}

ROOT_URLCONF = 'FluxyApi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'FluxyApi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

import os
from pathlib import Path

from django.conf import settings

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Utilisez le backend MySQL
        'NAME': 'Testdb',              # Remplacez par le nom de votre base de données MySQL
        'USER': 'root',            # Remplacez par votre nom d'utilisateur MySQL
        'PASSWORD': 'urbainP@tient123!',       # Remplacez par votre mot de passe MySQL
        'HOST': 'localhost',                     # Laissez 'localhost' si MySQL est sur le même serveur
        'PORT': '3306',                          # Le port par défaut pour MySQL est 3306
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# settings.py

ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'http://localhost:9200',
    },
}
from elasticsearch import Elasticsearch
from elasticsearch_dsl import connections
from django.conf import settings

# Créer une connexion Elasticsearch en utilisant la configuration
connections.create_connection(**settings.ELASTICSEARCH_DSL['default'])

# Test de la connexion
try:
    if connections.get_connection().ping():
        print("Connexion à Elasticsearch établie avec succès.")
    else:
        print("Connexion à Elasticsearch échouée.")
except Exception as e:
    print(f"Erreur de connexion : {e}")

# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


DEBUG = True  # Changez cela à True pour le développement

ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # Ajoutez d'autres hôtes si nécessaire


#Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'urbainpatient5@gmail.com'
EMAIL_HOST_PASSWORD = 'nngo chlw shwq jduf'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER 
ADMIN_EMAIL = 'urbainpatient5@gmail.com'

SILKY_PYTHON_PROFILER = True  # Activer le profiling Python
SILKY_PANELS = ['silk.panels.sql.SQLPanel', 'silk.panels.cache.CachePanel']  # Panneaux à afficher
SILKY_META = True  # Activer le suivi des métadonnées des requêtes
