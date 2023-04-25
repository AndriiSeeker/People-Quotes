from django.urls import path

from . import views


app_name = "quotes"

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:page>', views.home, name='root_paginate'),
]