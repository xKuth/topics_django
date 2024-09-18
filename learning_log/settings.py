from pathlib import Path
import os
import dj_database_url
import environ


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


env = environ.Env()

environ.Env.read_env()

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'True'

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'learning_logs',
    'users',
    #APP DE TERCEIROS
    'bootstrap3',
]

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

ROOT_URLCONF = 'learning_log.urls'

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

WSGI_APPLICATION = 'learning_log.wsgi.application'


# databases sqlite

DATABASES = { 
    "default":{
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Render PostergreSQL database (live)

database_url = os.environ.get("DATABASE_URL")
DATABASES["default"] = dj_database_url.parse(database_url)


# Password validation

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'learning_logs/static')
]

STATIC_STORAGE = "whitenoise.storage.compressedManifeStstatiFilesStorage"

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Url login page
LOGIN_URL = 'users/login'

# Bootstrap3
BOOTSTRAP3 = {
    'include_jquery': True
}


