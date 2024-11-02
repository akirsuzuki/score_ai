"""
Django settings for score project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'scoreai.apps.ScoreaiConfig',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     # 以下追加
    'rest_framework',
    'django_bootstrap5',
    'django.contrib.humanize',
    'crispy_forms',
    'crispy_bootstrap4',
    'widget_tweaks',
    'django_select2',
]


# 追加
AUTH_USER_MODEL = 'scoreai.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 静的ファイルのストレージ
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = 'score.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Add your custom context processor here
                'scoreai.context_processors.selected_company',
            ],
        },
    },
]

WSGI_APPLICATION = 'score.wsgi.application'

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ja'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ログインの挙動を追加
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'index'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Herokuデプロイ

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_URL = 'static/'

# 収集元
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'src', 'score', 'static'),  # 静的ファイルが含まれている最上位ディレクトリ
]
# 収集先
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

try:
    from .local_settings import *
except ImportError:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    DEBUG = False
    ALLOWED_HOSTS = ['.herokuapp.com', '0.0.0.0', '127.0.0.1']
    # EMAIL_HOST_USER = 'sth' or os.environ['EMAIL_HOST_USER']
    # EMAIL_HOST_PASSWORD = 'sth' or os.environ['EMAIL_HOST_PASSWORD']
    # STRIPE_PUBLIC_KEY = 'sth' or os.environ['STRIPE_PUBLIC_KEY']
    # STRIPE_SECRET_KEY = 'sth' or os.environ['STRIPE_SECRET_KEY']
    # AWS_ACCESS_KEY_ID = 'sth' or os.environ['AWS_ACCESS_KEY_ID']
    # AWS_SECRET_ACCESS_KEY = 'sth' or os.environ['AWS_SECRET_ACCESS_KEY']
    import dj_database_url
    # DATABASES['default'] = dj_database_url.config()
    DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
    pass
