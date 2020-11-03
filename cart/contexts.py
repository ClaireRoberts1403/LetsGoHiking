from django.conf import settings
from django.shortcuts import get_object_or_404
from shop.models import Product


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += item_data * product.price
        product_count += item_data
        cart_items.append({
            'item_id': item_id,
            'quantity': item_data,
            'product': product,
        })

    delivery = 1

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
