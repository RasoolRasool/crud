from django.contrib import admin
from django.urls import path,include
from authapi import views
urlpatterns = [
    path('login/',views.LoginView.as_view()),
    path('logout/',views.LogOutView.as_view())
]