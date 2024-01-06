from .models import CartItem


def count_cart_items(request):
    cart_items_count = CartItem.objects.filter(cart__user=request.user).count()
    return {'cart_items_count': cart_items_count}