from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    # Страница для добавления новой темы.
    path('new_topic/', views.new_topic, name='new_topic'),

]