from django.urls import Path

from . import views

urlpatterns = [
    path('', views.index, name='index.html'),
]