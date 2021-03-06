#import os
from decouple import config
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY =config('app_secret_key')

DEBUG =config('django_debug') 

# SECURITY WARNING: don't run with debug turned on in production!

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'company',
    'users',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'dj_rest_auth',
    'dj_rest_auth.registration',
     'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    
]

ROOT_URLCONF = 'invauthproject.urls'

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

WSGI_APPLICATION = 'invauthproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {

    'default': {

        'ENGINE':  config('db_engine'),
        'HOST': config('db_host'),
        'NAME': config('db_name'),
        'USER': config('db_user'),
        'PASSWORD':  config('db_pwd'),
        'PORT': config('db_port'),
        
    }

}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#-- additional
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     ],
# }
REST_FRAMEWORK = {
'DEFAULT_PERMISSION_CLASSES': (
    'rest_framework.permissions.IsAuthenticated',
),
'DEFAULT_AUTHENTICATION_CLASSES': (
    'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
),
}

# REST_FRAMEWORK = { 'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',)
# , 'DEFAULT_AUTHENTICATION_CLASSES': ( 'rest_framework.authentication.TokenAuthentication'
# , 'rest_framework_jwt.authentication.JSONWebTokenAuthentication'
# , 'rest_framework.authentication.SessionAuthentication'
# , 'rest_framework.authentication.BasicAuthentication', )
# , 'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning', } 

SITE_ID = 1
REST_USE_JWT = True
JWT_AUTH_COOKIE = 'JWT' # what the cookie will be called 

# to handle authentication while login
AUTHENTICATION_BACKENDS = [
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
]

#mandatory email verification
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# allow the website to verify the user when the user opens the link received in the email. Then, we want the user to be redirected to the LOGIN_URL after verification, so we specified our LOGIN_URL
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
LOGIN_URL = 'http://localhost:8000/users/login'

# Email backend Config
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER =config('mail_id')
EMAIL_HOST_PASSWORD =config('mail_pd')
EMAIL_PORT = 587


AUTH_USER_MODEL = 'users.User'

ACCOUNT_USERNAME_REQUIRED = False

# REST_AUTH_REGISTER_SERIALIZERS = {
#     'REGISTER_SERIALIZER': 'users.serializers.CustomRegisterSerializer'
# }

ACCOUNT_ADAPTER = 'users.adapters.CustomUserAccountAdapter'


# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'invauthproject.users.views.JWTAuthentication',
#     ),
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticated',
#     )
# }

from corsheaders.defaults import default_headers


# CORS_ALLOW_HEADERS = default_headers + ('content-disposition', 'accept-encoding',
#                       'content-type', 'accept', 'origin', 'authorization','Token')

ALLOWED_HOSTS=['*']
#ALLOWED_HOSTS = [*]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]
