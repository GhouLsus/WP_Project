import os
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^rz9wrbb#ig!tl)4c$!o_^01ef8(rtxe(i()$ph61$8+mh^v_8'

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
    'constance',
    'constance.backends.database',
    'ckeditor',
    'ckeditor_uploader',
    'content.apps.ContentConfig',
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

ROOT_URLCONF = 'PyEditorial.urls'

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
                'content.context_processors.show_system_content',
            ],
        },
    },
]

WSGI_APPLICATION = 'PyEditorial.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# If you need to use Postgresql, you can use this section
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'PyEditorial',
#         'USER': 'postgres',
#         'PASSWORD': 'great123',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGES = [
    ('en', _('English')),
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "templates/static"),
]

# Media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# CKEditor
CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    },
}

# CONSTANCE Settings
CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

CONSTANCE_IGNORE_ADMIN_VERSION_CHECK = True

# Cache Settings
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'django_cache'),
    }
}
CONSTANCE_DATABASE_CACHE_BACKEND = 'default'

CONSTANCE_ADDITIONAL_FIELDS = {
    'yes_no_select': ['django.forms.fields.ChoiceField', {
        'widget': 'django.forms.Select',
        'choices': (
            ("yes", _('Yes')),
            ("no", _('No'))
        )
    }],
    'image_field': ['django.forms.ImageField', {}]
}

CONSTANCE_CONFIG = {
    'SITE_TITLE': ('My Blog', _('Title of this site!'), str),
    'SITE_DESCRIPTION': ('Blog Description', _('Description of this site!'), str),
    'SITE_FAVICON': ('default_favicon.png', _('Favicon of this site!'), 'image_field'),

    'GET_IN_TOUCH_ACTIVE': ('yes', _('"Get in touch" section is active?'), 'yes_no_select'),
    'GET_IN_TOUCH_INFO': ('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', _('"Get in touch" information text'), str),
    'GET_IN_TOUCH_EMAIL_ADDRESS': ('information@untitled.tld', _('"Get in touch" email address'), str),
    'GET_IN_TOUCH_PHONE': ('(000) 000-0000', _('"Get in touch" phone number'), str),
    'GET_IN_TOUCH_ADDRESS': ('1234 Somewhere Road #8254<br />Nashville, TN 00000-0000', _('"Get in touch" address'), str),

    'SOCIAL_NETWORKS_FACEBOOK_URL': ('#', _('Social Networks - Facebook'), str),
    'SOCIAL_NETWORKS_TWITTER_URL': ('#', _('Social Networks - Twitter'), str),
    'SOCIAL_NETWORKS_SNAPCHAT_URL': ('#', _('Social Networks - Snapchat'), str),
    'SOCIAL_NETWORKS_INSTAGRAM_URL': ('#', _('Social Networks - Instagram'), str),
    'SOCIAL_NETWORKS_MEDIUM_URL': ('#', _('Social Networks - Medium'), str),
    'SOCIAL_NETWORKS_TELEGRAM_URL': ('#', _('Social Networks - Telegram'), str),
    'SOCIAL_NETWORKS_GITHUB_URL': ('#', _('Social Networks - Github'), str),
    'SOCIAL_NETWORKS_GITLAB_URL': ('#', _('Social Networks - Gitlab'), str),
}

CONSTANCE_CONFIG_FIELDSETS = {
    'General Options': (
        'SITE_TITLE',
        'SITE_DESCRIPTION',
        'SITE_FAVICON',
    ),
    '"Get in touch" Options': (
        'GET_IN_TOUCH_ACTIVE',
        'GET_IN_TOUCH_INFO',
        'GET_IN_TOUCH_EMAIL_ADDRESS',
        'GET_IN_TOUCH_PHONE',
        'GET_IN_TOUCH_ADDRESS',
    ),
    '"Social Networks" Options': (
        'SOCIAL_NETWORKS_FACEBOOK_URL',
        'SOCIAL_NETWORKS_TWITTER_URL',
        'SOCIAL_NETWORKS_SNAPCHAT_URL',
        'SOCIAL_NETWORKS_INSTAGRAM_URL',
        'SOCIAL_NETWORKS_MEDIUM_URL',
        'SOCIAL_NETWORKS_TELEGRAM_URL',
        'SOCIAL_NETWORKS_GITHUB_URL',
        'SOCIAL_NETWORKS_GITLAB_URL',
    ),
}

# Auth Settings
LOGIN_REDIRECT_URL = 'content:index'
LOGIN_URL = 'login'
LOGOUT_REDIRECT_URL = 'content:index'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
