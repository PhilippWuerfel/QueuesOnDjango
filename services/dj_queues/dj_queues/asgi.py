"""
ASGI config for dj_queues project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from polls import routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj_queues.settings")

application = get_asgi_application()

application = ProtocolTypeRouter(
    {"http": get_asgi_application(), "websocket": URLRouter(routing.urlpatterns)}
)
