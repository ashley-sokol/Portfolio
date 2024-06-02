from django.urls import path
from django.urls import path, include
from .views import *
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
app_name = 'portfolio_site'

from . import views

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]