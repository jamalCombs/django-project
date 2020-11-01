from django.urls import path
from django.conf.urls.static import static
from .views import analytic_view

urlpatterns = [
    path('analytics/', analytic_view, name='analytics'),
]
