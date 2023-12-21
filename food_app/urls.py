from django.urls import path
from . import views


#create food app urls here
urlpatterns = [
    path('', views.index, name='home'),
    path('foods/', views.foods, name='foods'),
    path('food_details/<pk>/', views.food_details, name='food_details'),
]
