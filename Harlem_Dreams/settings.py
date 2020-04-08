"""
Django settings for Harlem_Dreams project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u18&d+)o1v$5@7xdhqivvbw!2u1&dlbwtqdc41+4s6=^m7q$dl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    'harlemdreams.net',
    'www.harlemdreams.net',
    'www.theharlemdreams.net',
    'theharlemdreams.net',
    '107.180.89.232',
    'theharlemdreams.com',
    'www.theharlemdreams.com',
]

# Application definition

INSTALLED_APPS = [
    'apps.dream_app',
    'apps.newsletters',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Imperavi (or tinymce) rich text editor is optional
    # 'imperavi',
    'sorl.thumbnail',
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

ROOT_URLCONF = 'Harlem_Dreams.urls'

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

WSGI_APPLICATION = 'Harlem_Dreams.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
   }
}

# DATABASES = {
#      'default': {
#          'ENGINE': 'django.db.backends.postgresql',
#          'NAME': 'hdreamsdb',
#          'USER': 'admin',
#          'PASSWORD': 'bluemonkey',
#          'HOST': 'localhost',
#          'PORT': '5432',
#      }
#  }

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/


# STATIC_ROOT = "app-root/Harlem_Dreams/wsgi/static"

STATICFILES_DIR = (os.path.join(BASE_DIR, "/dream_app/static"))

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,  'media/') 



# SMTP
EMAIL_USE_TLS = True
EMAIL_HOST = 'p3plcpnl0122.prod.phx3.secureserver.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'contact@harlemdreams.net'
EMAIL_HOST_PASSWORD = 'Longbeach2018'

# reCAPTCHA

GOOGLE_RECAPTCHA_SECRET_KEY = '6LcHqXAUAAAAAAUE04nczeIVXmHxCv4C-_uo85Wj'


# NEWSLETTER


# NEWSLETTER_CONFIRM_EMAIL = False

# NEWSLETTER_RICHTEXT_WIDGET = "imperavi.widget.ImperaviWidget"
# # Using django-tinymce
# NEWSLETTER_RICHTEXT_WIDGET = "tinymce.widgets.TinyMCE"

# # Amount of seconds to wait between each email. Here 100ms is used.
# NEWSLETTER_EMAIL_DELAY = 0.1
# # Amount of seconds to wait between each batch. Here one minute is used.
# NEWSLETTER_BATCH_DELAY = 60
# # Number of emails in one batch
# NEWSLETTER_BATCH_SIZE = 100
