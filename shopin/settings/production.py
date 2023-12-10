from .base import *


DEBUG = False
print("hiiiiiiiiiiiiiiiiiiiiiiii", DEBUG)


ALLOWED_HOSTS = ["*"]

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'shopin_user',
        'PASSWORD': '12345shopin',
        'HOST': 'db',
        'PORT': '5432',
        'NAME': 'shopin_db',
    }
}

STATIC_URL = '/public/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'public', 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'public', 'media')
