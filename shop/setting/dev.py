from shop.settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ttrqwwfyy-t%jip@oxhwcg(fg3_+sc)-q152@zf@c@vbx&o_ph'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []




# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#sites framework
SITE_ID = 3

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'website/static'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
COMPRESS_ROOT = BASE_DIR / 'static'