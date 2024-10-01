from shop.settings import *
from decouple import config
import dj_database_url
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ttrqwwfyy-t%jip@oxhwcg(fg3_+sc)-q152@zf@c@vbx&o_ph'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost',
  '127.0.0.1',]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'website/static'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# STATICFILES_DIRS = [
#      BASE_DIR/"website/static",
# ]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config('DB_PROD_NAME'),                      
#         'USER':  config('DB_PROD_USER'),
#         'PASSWORD': config('DB_PROD_PASSWORD'),
#         'HOST': '',
#         'PORT': config('DB_PROD_PORT',cast = int),
#     }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
# DATABASES = {
#     'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': 'root',
#         'PASSWORD': 'ZUutuNnORxNLZseNhfsACik0',
#         'HOST': 'tai.liara.cloud',
#         'PORT': '33004',
    # }}
# DATABASES = {
#     'default': dj_database_url.config(default=config('DATABASE_URL')) 
#     }


