from django.shortcuts import render, redirect
from .models import Product
from .forms import *
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    return render(request, 'index.html')


# def foods(request):
#     products = Product.objects.all()
#     return render(request, 'food-page.html', {'products': products})


def food_details(request, pk):
    product = Product.objects.get(id=pk)
    reviews = Review.objects.filter(product=product)
    
    return render(request, 'single-food.html', {'product': product, 'reviews': reviews})



# views.py
def filter_items(request):
    items = Product.objects.all()

    return render(request, 'food-page.html', {'items': items})


@login_required(login_url='login')
def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('filter-items')


@login_required(login_url='login')
def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, 'cart.html', {'cart_items': cart_items})



# @require_POST
# def update_quantity(request):
#     cart_item_id = request.POST.get('cart_item_id')
#     action = request.POST.get('action')

#     cart_item = get_object_or_404(CartItem, id=cart_item_id)

#     if action == 'increment':
#         cart_item.quantity += 1
#     elif action == 'decrement':
#         if cart_item.quantity > 1:
#             cart_item.quantity -= 1

#     cart_item.save()

#     data = {
#         'new_quantity': cart_item.quantity,
#     }

#     return JsonResponse(data)
