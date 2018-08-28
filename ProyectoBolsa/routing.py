from django.urls import path

from channels.routing import ProtocolTypeRouter, URLRouter

from AppCheckCeleryChannels.consumers import Consumidor
from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
    
        URLRouter([
            path("checks/Crear_Chat/", Consumidor),
        ]),
    ),  
})
