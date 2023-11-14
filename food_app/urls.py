from django.urls import path
from . import views


#create food app urls here
urlpatterns = [
    path('', views.index, name='home'),
]
