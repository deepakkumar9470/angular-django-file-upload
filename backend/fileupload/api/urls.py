from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('upload/', views.home.as_view({'get':'list'}), name='home' ),
]
