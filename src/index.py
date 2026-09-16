import os

from django.core.asgi import get_asgi_application
from workers import asgi

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = get_asgi_application()

Default = asgi.entrypoint(app)