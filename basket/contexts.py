from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404

from products.models import Product


def basket_contents(request):
    basket_items = []
    total = 0
    product_count = 0
    item_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        item_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = Decimal(settings.STANDARD_DELIVERY_FEE)
        free_delivery_delta = Decimal(settings.FREE_DELIVERY_THRESHOLD) - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total
    product_count = len(basket_items)

    context = {
        'basket_items': basket_items,
        'product_count': product_count,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
