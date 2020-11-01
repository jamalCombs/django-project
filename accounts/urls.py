from django.urls import path
from django.conf.urls.static import static
from .views import (
    home_view, 
    login_view, 
    register_view)

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
]
