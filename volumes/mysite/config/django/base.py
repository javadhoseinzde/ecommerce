from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1p6)b)#&x3b3=5k2ai6=f^zs00fpkxp$fcj#m!x3=5yxldp5on'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost", "app"]


# CSRF_TRUSTED_ORIGINS = [
#     'localhost',
#     'http://127.0.0.1:8000'
# ],

CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1:7001',
    'http://hesss.drlink.ir'
       
]

CORS_ORIGIN_WHITELIST = [
    'http://127.0.0.1:8000'
]


LOCAL_APPS = [
    'app.antmedia_api.apps.AntmediaApiConfig',
]



# Application definition
LOCAL_APPS = [
    'app.common.apps.CommonConfig',
    'app.shop.apps.ShopConfig',
    'app.users.apps.UsersConfig',
    'app.category.apps.CategoryConfig',
    'app.comments.apps.CommentsConfig',
    'app.cart.apps.CartConfig',
    'app.order.apps.OrderConfig',
    'app.static_pages.apps.StaticPagesConfig',
    'app.utils.apps.UtilsConfig'



]



THIRD_PARTY_APPS = [
    'rest_framework',
    'rest_framework_simplejwt',
    'ckeditor',
    'ckeditor_uploader',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    *THIRD_PARTY_APPS,
    *LOCAL_APPS,
]

CKEDITOR_BASEPATH = '/static/ckeditor/ckeditor/'
CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_CONFIGS = {
        'default':{
                'toolbar': 'full',
                'allowedContent': True,
        }
}



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

TIME_ZONE = 'Asia/Tehran'


USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

from config.settings.sessions import *  # noqa
from config.settings.celery import *  # noqa
from config.settings.kavenegar import *  # noqa
from config.settings.jwt import *  # noqa

AUTH_USER_MODEL = 'users.MyUser'
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'app.users.mybackend.ModelBackend',
]

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static_root")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
LOGOUT_REDIRECT_URL = "/"