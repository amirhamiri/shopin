from .base import *

from corsheaders.defaults import default_headers

DEBUG = False
print("hiiiiiiiiiiiiiiiiiiiiiiii", DEBUG)
CORS_ALLOW_HEADERS = list(default_headers) + [
    "same-origin", "client", "Access-Control-Allow-Origin"
]

CORS_ALLOWED_ORIGINS = ["*"]

ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'USER': 'root',
#         'PASSWORD': '1234',
#         'HOST': 'mysql-service',
#         # 'PORT': '80',
#         'NAME': 'mysql_db',
#     }
# }

STATIC_URL = '/public/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'public', 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'public', 'media')
