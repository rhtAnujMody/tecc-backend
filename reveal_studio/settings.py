"""
Django settings for reveal_studio project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os


from dotenv import load_dotenv
load_dotenv()
# from dotenv import load_dotenv
# load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', default='secret')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'studio',
    'auditlog',
    'rest_framework_simplejwt',
    'djoser',
    'corsheaders',
    'rest_framework',
]

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_USE_TLS = True
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD =os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL =os.environ.get('DEFAULT_FROM_EMAIL')
DOMAIN = os.environ.get("DOMAIN")
SITE_NAME = "Reveal Studio"

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
"https://domain.com",
"https://api.domain.com",
"http://localhost:3000",
"http://127.0.0.1:9000"
]

CORS_ALLOW_METHODS = [
'DELETE',
'GET',
'OPTIONS',
'PATCH',
'POST',
'PUT',
]

CORS_ALLOW_HEADERS = [
'accept',
'accept-encoding',
'authorization',
'content-type',
'dnt',
'origin',
'user-agent',
'x-csrftoken',
'x-requested-with',
]

ROOT_URLCONF = 'reveal_studio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR /"studio", 'templates')],
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

WSGI_APPLICATION = 'reveal_studio.wsgi.application'


CORS_ALLOW_ALL_ORIGINS = True


CORS_ALLOW_CREDENTIALS = True

CORS_EXPOSE_HEADERS = [
    'Total-Pages',
]

CORS_ORIGIN_WHITELIST = (
    os.environ.get('CORS_ORIGIN', "http://localhost:3000"),"http://localhost:3000",
)

CSRF_TRUSTED_ORIGINS = [
    os.environ.get('CSRF_TRUSTED_ORIGIN', "http://localhost:8000"),
]


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME', 'studioDB'),
        'USER': os.environ.get('DB_USER', 'root'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'password'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '3306'),
    }
}



REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES":(
        'rest_framework_simplejwt.authentication.JWTAuthentication',

    )
}

JWT_SECRET_KEY=os.environ.get('JWT_SECRET_KEY') 

from datetime import timedelta

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES":(
        "Bearer",
        "JWT",
    ),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=6000),
    "REFRESH_TOKEN_LIFETIME": timedelta(minutes=6000),
    "SIGNING_KEY": os.environ.get('SIGNING_KEY'),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
}


DJOSER ={
    "LOGIN_FIELD": "email",
    "USER_CREATE_PASSWORD_RETYPE": True,
    "USERNAME_CHANGE_EMAIL_CONFIRMATION": True,
    "SEND_CONFIRMATION_EMAIL": True,
    "PASSWORD_RESET_CONFIRM_URL":"password/reset/confirm/{uid}/{token}",
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    "SET_PASSWORD_RETYPE": True,
    "PASSWORD_RESET_CONFIRM_RETYPE": True,
    "USERNAME_RESET_CONFIRM_URL": "email/reset/confirm/{uid}/{token}",
    "ACTIVATION_URL": "activate/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": True,
    "SERIALIZERS":{
        'user_create': "studio.serializers.UserCreateSerializer",
        'user': "studio.serializers.UserSerializer",
        'current_user': "studio.serializers.UserSerializer",
        'delete_user': "djoser.serializers.UserDeleteSerializer"

    }
} 

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# if os.environ.get('USE_S3') == 'TRUE':
#     AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
#     AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
#     AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
#     AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
#     AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME', 'ap-northeast-1')
#     AWS_S3_SIGNATURE_VERSION = 's3v4'
#     DEFAULT_FILE_STORAGE = 'core.storage.storage_backends.PrivateMediaStorage'
#     AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=8400'}
#     AWS_S3_FILE_OVERWRITE = False

# else:
#     MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
#     MEDIA_URL = '/media/'


DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_QUERYSTRING_AUTH = False
AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME')
#check for expiry 

AWS_S3_CUSTOM_DOMAIN = os.environ.get('AWS_S3_CUSTOM_DOMAIN')


STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / STATIC_URL

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = "studio.user"

import logging
import logging.config
from django.utils.log import DEFAULT_LOGGING

logger = logging.getLogger(__name__)

LOG_LEVEL = "INFO"

logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        #formatters configuration
        "formatters":{
            "console":{
                "format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s" 
            },
            "file": {"format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"},
            "django.server": DEFAULT_LOGGING["formatters"]["django.server"],
        },
        #handlers configuration
        "handlers":{
            "console":{
                "class": "logging.StreamHandler",
                "formatter": "console"
            },

            "file":{
                "level": "INFO",
                "class": "logging.FileHandler",
                "formatter": "file",
                "filename": "logs/tecc.log",
            },
             "django.server": DEFAULT_LOGGING["handlers"]["django.server"],
        },
        #loggers configuration
        "loggers": {
            "": {"level":"INFO", "handlers": ["console", "file"], "propagate": False},
            "apps": {"level":"INFO", "handlers": ["console", "file"], "propagate": False},
            "django.server": DEFAULT_LOGGING["loggers"] ["django.server"],

        }
    }
)

