from django.urls import path
from django.conf.urls.static import static
from .views import chat_view

urlpatterns = [
    path('chat/', chat_view, name='chat'),
]
