import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from django.urls import path
from messaging import consumers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            [
                path('messaging/chat/', consumers.ChatConsumer.as_asgi()),
            ]
        )
    ),
})