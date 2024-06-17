from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.add_food, name='add_food'),
    path('add/', views.add_food, name='add_food'),
    path('view/', views.view_food, name='view_food'),
    path('remove/<int:food_id>/', views.remove_food, name='remove_food'),
    path('reset/', views.reset_calories, name='reset_calories'),
]
