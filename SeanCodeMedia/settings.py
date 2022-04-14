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
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'boxingstudiogames237@gmail.com'
EMAIL_HOST_PASSWORD = 'Rosezaten5000$'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
   '127.0.0.1',
 ]



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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# START
CKEDITOR_UPLOAD_PATH = 'uploads/'
MEDIA_URL = '/src/media/' 
MEDIA_ROOT =  os.path.join(BASE_DIR,'media')

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