from django.contrib import admin
from django.urls import path, include
from users import views

urlpatterns = [
    path('register/', views.register_request, name = 'register'),    
    path('login/', views.login_request, name = 'login'),
]