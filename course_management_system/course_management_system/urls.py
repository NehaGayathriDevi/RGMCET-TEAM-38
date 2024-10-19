"""
URL configuration for course_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include  # include is optional if you're not using it
from . import views  # Import your views if you're using them

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),  # If you have a separate app for courses
    path('teachers/', include('teachers.urls')),  # If you have a separate app for teachers
    path('select-courses/', views.select_courses, name='select_courses'),  # Your select courses view
]

