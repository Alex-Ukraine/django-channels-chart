from django.urls import path

from .consumers import GraphConsumer
# views / consumers
ws_urlpatterns = [
    path('ws/graph/', GraphConsumer.as_asgi())
]
