from django.urls import path
from . import views


#create food app urls here
urlpatterns = [
    path('', views.index, name='home'),
    # path('foods/', views.foods, name='foods'),
    path('food_details/<pk>/', views.food_details, name='food_details'),
    path('filter/', views.filter_items, name='filter-items'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
]
