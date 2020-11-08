from django.urls import path
from django.conf.urls.static import static
from .views import (
    CourseListView,
    CourseCreateView,
)

urlpatterns = [
    path('', CourseListView.as_view(), name='course-list'),
    path('create/', CourseCreateView.as_view(), name='course-create')
]
