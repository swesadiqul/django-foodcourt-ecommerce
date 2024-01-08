from .models import CartItem


def count_cart_items(request):
    if request.user.is_authenticated:
        cart_items_count = CartItem.objects.filter(cart__user=request.user).count()

    else:
        cart_items_count = 0

    context = {'cart_items_count' : cart_items_count}
    
    return context