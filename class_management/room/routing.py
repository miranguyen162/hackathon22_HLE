from calendar import c
from importlib.resources import path
from django.urls import path

from room import consumers

websocket_urlpatterns = [
    path("ws/<str:room_name>", consumers.ChatConsumer.as_asgi())

]