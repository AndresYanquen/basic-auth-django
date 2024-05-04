from django.urls import re_path, path, include

from . import views

urlpatterns = [
    path('scheduler', views.ListUsers.as_view(), name="listUsers")
]
