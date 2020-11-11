from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from .views import (
    LoginView,
    AccountHomeView,
    RegisterView,
)


app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('home/', AccountHomeView.as_view(), name='home'), 
    path('register/', RegisterView.as_view(), name='register'),
]
