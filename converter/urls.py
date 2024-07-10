from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.MainPageView.as_view(), name='main_page'),
]
