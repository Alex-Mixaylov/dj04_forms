from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_movie, name='add_movie'),
    path('films/', views.view_movies, name='films'),
]
