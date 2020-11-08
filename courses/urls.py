from django.urls import path
from django.conf.urls.static import static
from .views import (
    CourseListView
)

urlpatterns = [
    path('courses/', CourseListView.as_view(), name='course-list'),
]
