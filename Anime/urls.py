from django.urls import path, include
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
]
