from django.urls import path
from django.conf.urls.static import static
from .views import course_list_view

urlpatterns = [
    path('courses/', course_list_view, name='course-list'),
]
