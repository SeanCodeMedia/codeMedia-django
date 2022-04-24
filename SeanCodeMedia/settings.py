"""
Django settings for SeanCodeMedia project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from django.core.management.utils import get_random_secret_key
from pathlib import Path
#EMAIL 
EMAIL_HOST = str(os.environ.get('EMAIL_HOST'))
EMAIL_HOST_USER = str(os.environ.get('EMAIL_HOST_USER'))
EMAIL_HOST_PASSWORD = str(os.environ.get('EMAIL_HOST_PASSWORD'))
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_USE_TLS = True


# EMAIL_HOST            = 'smtp.gmail.com'
# EMAIL_USER_HOST       = 'boxingstudiogames237@gmail.com'
# EMAIL_HOST_PASSWORD   = 'Rosezaten5000$'
# EMAIL_PORT            = 587 
# EMAIL_USE_TLS         = True


AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID") 
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_ENDPOINT_URL = os.environ.get("AWS_S3_ENDPOINT_URL")
# I enabled the CDN, so you get a custom domain. Use the end point in the AWS_S3_CUSTOM_DOMAIN setting. 
AWS_S3_CUSTOM_DOMAIN = os.environ.get("AWS_S3_CUSTOM_DOMAIN") # check this but to add custom CDN URLs
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = str(os.environ.get("DEBUG")) == "1"
print("WARING - DEBUG " + str(DEBUG))
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost,seancodemedia-django-app-dwjik.ondigitalocean.app,seancodemedia.com").split(",")

DEVELOPMENT_MODE = os.environ.get("DEVELOPMENT_MODE", "False") == "True"

import mimetypes
mimetypes.add_type("application/javascript", ".js", True)
mimetypes.add_type("text/css", ".css", True)
mimetypes.add_type("text/html",".html", True)
# Application definition

INSTALLED_APPS = [
    #My apps 
    'home',
    'SeanCodeMedia',
     'blog',
     'contact',
     'portfolio',
     'ckeditor',
     'videos',
     'ckeditor_uploader',
     'admin_interface',
     'colorfield',
     'templatetags',


    # Django apps 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',

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

ROOT_URLCONF = 'SeanCodeMedia.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
        os.path.join(BASE_DIR,"templates")
        ],
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

WSGI_APPLICATION = 'SeanCodeMedia.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'CodeMediaDB',
        'USER': 'doadmin',
        'PASSWORD': 'do3i3vAeccORcevv',
        'HOST': 'codemedia-db-do-user-866838-0.b.db.ondigitalocean.com',
        'PORT': '25060',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# START
CKEDITOR_UPLOAD_PATH = 'uploads/'
# MEDIA_URL = '/media/' 
# MEDIA_ROOT =  os.path.join(BASE_DIR,'media')

 # uncomment if you want to host static files from spaces 
 # https://www.digitalocean.com/community/questions/how-to-store-django-media-files-to-spaces

# STATIC_URL = '{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, 'static')
# STATIC_ROOT = 'static/'
# STATICFILES_STORAGE = 'custom_storages.StaticStorage'
MEDIA_URL_DOWNLOAD = 'https://'+'{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, 'media')
print(MEDIA_URL_DOWNLOAD)
MEDIA_URL = '{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, 'media')
MEDIA_ROOT = 'media/'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
AWS_DEFAULT_ACL = 'public-read'
DISABLE_COLLECTSTATIC=1
# END

# ckeditor 

CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"


#https://django-ckeditor.readthedocs.io/en/latest/#widget
CKEDITOR_CONFIGS = {
   'default': {
        'skin': 'moono-dark',
        'toolbar':[ 

           ['CodeSnippet', ],

            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ["Image","Table", 'RemoveFormat'],
            ['Styles', 'Format', 'Font', 'FontSize'],
            ['TextColor', 'BGColor', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe'],
         ],

       # 'skin': 'moono-dark',
        'extraPlugins': 'codesnippet',

   },
}
