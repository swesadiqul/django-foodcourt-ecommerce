from django.shortcuts import render
from .models import Product
from .forms import *


# Create your views here.
def index(request):
    return render(request, 'index.html')


def foods(request):
    foods = Product.objects.all()
    return render(request, 'food-page.html', {'foods': foods})


def food_details(request, pk):
    product = Product.objects.get(id=pk)
    reviews = Review.objects.filter(product=product)
    
    return render(request, 'single-food.html', {'product': product, 'reviews': reviews})