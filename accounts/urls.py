from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from .views import (
    LoginView,
)

app_name = 'accounts'

urlpatterns = [
    url('', LoginView.as_view(), name='login'),
]
