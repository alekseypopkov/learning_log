"""Определяет схемы URL для пользователей."""
from django.urls import path, include

from . import views

app_name = 'accounts'
urlpatterns = [
    # Добавить URL авторизации по умолчанию.
    path('', include('django.contrib.auth.urls')),

    # Страница регистрации.
    path('register/', views.register, name='register'),
]