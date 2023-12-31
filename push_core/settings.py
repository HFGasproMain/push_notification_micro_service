"""
Django settings for push_core project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from firebase_admin import initialize_app

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-(-a6kt#013v#ajgt8w$g+6qn3n4a(l1@*%w&63ym151n^jtxot"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # installed apps
    'core',
    'fcm_django',
    'rest_framework',
    'drf_yasg',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "push_core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "push_core.wsgi.application"


XFCM_DJANGO_SETTINGS = {
    "FCM_SERVER_KEY": 
    "MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQD6+TJjjN0kWCTw \
   V4p2h7WRsvFO3PMwJm4Ur83Ig9fJ8eMrXMYvS5P7NjVxwaHd2h/9Q3YhwiTIX9aP \
   gU/RaHeoPHZKj38Pnzc7wbiMXfiZgOhBkO7cx+r4+YQp4s6Fw66kY2rPWMA/ms5g \
   3O/R5DRMpb2yDqw6NDhPkwtVaklv2LbTs8zqS7ALxUurM0YvB7PboMESGqsl9EgJ \
   U/YyhuFo+rV/eLlrdRqc/hCKjHmtaqsVh7gM70EIuWJqnBNg57MzS5chjbU2IuxF \
   T9bnLebAvbRbQDKa41rjYyTkSj8gU17aX89o8h/aXhbgEmHKS/frqOi9nFiYeb/f \
   rlcxadFJAgMBAAECggEAF8d7tD35CAQH//OzbVafZ/4l6fx6WEIT5QbhPxHq5Lnz \
   9bxVFM8a5s70kmIv1YbgyAzXyQwNkyStfixY5TT6PWj5JkhhWBgUUiehNj+DGfxC \
   RVAXqbiRdWSi1pskST1Is0+uI5Y7pOskib31RRRTtj1v80p7nAotmbCLftzSt3OH \
   mo8mAkLAtkwPLX+0Xu1wAgJ8bg6DnGsAUzrElftOy5xfdXtoZ57Lv2Q3+pUZWQIH \
   v8IEDvpa1SBqxBsw4oSdplLUetOEalfLzQ/GRz6M45Hr4IQMtoxxDyzDzhxt8LUj \
   f6FTHSgxSdnUvkL3voJ1HiO5vdEAVJPYXTlC6K4GwQKBgQD+TADomCgNafsfLiv3 \
   GWOELQRg9bE16moojd49EW6JpP/dbPBRYGnrp+4MQI+N0OEXr9b0sLTSrSJOPyex \
   bnPYiFJl3qWPt/+bytYD/4VEWkBHBuOGaYXMK1Pgn6Z+jv0zhkdHPZR62PUEZI6Y \
   DZ9nXkP/+BxW/92HmGpkMAUxMQKBgQD8p37B4RqrZAUxBV8gzTaQ4JQSFjrtGnM7 \
   XOgdkaZMD3W3+6hCUbLhXCxNziNuLRRlycIrJl5ZBgNN8tn8vxVgD5GI7Kjk3/tb \
   /JXtP4/kgMz6H3MxntZ4568qwO4KmyU5YDlRa6Wb2e42HpnIUMuAGUOFKjqDBokC \
   qN2TpkNbmQKBgGeUAZK71ySPlG/A2LuPJc/CnlP3/zRcxNy73Fe3b/S0tls0cjZT \
   NRF9lyJ6cX5sJCMHxmBoUV62kpCYfMxyltENxbIkm/8MDRsh5UY/n8KVmDTWA3rO \
   JGdjBokpviEykMOZ4BKObJoVIMenRcV9Vv49kSkDoFd3ZH5EgKFKRfMhAoGAd6/J \
   BoNipOp+4xgOVnWgccVRn7fUNlofWHHMq6VByCpSs9ONg808FjIZ8snCUwEb9pQ7 \
   XUGR1E5a5mQzC95he94kLV8fKz1Hz+26AGfp/G9fquWXJlx+cUwf2PsISRHx8lo5 \
   DO8XxtrYU97vLsvHe2l8aOr2SPehlBb20Gkk45ECgYEApovWUNlS6RbYRxxBR8Bq \
   9ovdPBAs7afQDh+ea/kcLKQjzcOs5hoomADeBnsWYUMF7KPzMD5oaJSCYrfTODr4 \
   /iza0JY6y0BCY8/PfvyYI3/SWjK2zHUQnrfOg5uopOSctyK+5AYhtYsqBfTzA6JR \
   HODmZzLiXzyo0mU2A3D5JU0"

}

FCM_DJANGO_SETTINGS = {
    "FCM_SERVER_KEY": "AIzaSyCTIDvk2ryZIh_D0i_7xsu4VyC0bQuL52E"}

# Initialize firebase app
FIREBASE_APP = initialize_app()


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
