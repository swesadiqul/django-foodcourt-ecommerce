from django.urls import path
from . import views


#create users app urls here
urlpatterns = [
    path('register/', views.register, name='signup'),
    path('login/', views.signin, name='login'),
]
