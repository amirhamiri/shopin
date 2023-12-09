import os

from django.core.wsgi import get_wsgi_application

if os.environ.get('DJANGO_ENV') == 'production':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shopin.settings.production")
else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shopin.settings.development")

application = get_wsgi_application()
