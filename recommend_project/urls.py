"""recommend_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from accounts.views import home_view, login_view, register_view
from chat.views import chat_view
from courses.views import course_list_view
from analytics.views import analytic_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # Accounts
    path('accounts/', include('accounts.urls')),
    
    # Chat
    path('', include('chat.urls')),

    # Courses
    path('', include('courses.urls')),

    # Analytics
    path('', include('analytics.urls')),
]
