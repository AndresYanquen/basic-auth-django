from django.urls import re_path, path, include

from . import views

urlpatterns = [
    re_path('signup', views.signup),
    re_path('login', views.login),
    re_path('test_token', views.test_token),
    path('', include('scheduler.urls'))
]
