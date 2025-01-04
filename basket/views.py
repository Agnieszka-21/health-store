from django.contrib import messages
from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)

from products.models import Product


def view_basket(request):
    """
    Renders the basket contents page
    """
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """
    Adds a quantity of the specified product to the shopping basket
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(
            request, f'Updated {product.name} quantity in your basket')
    else:
        basket[item_id] = quantity
        messages.success(request, f'Added {product.name} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def update_basket(request, item_id):
    """
    Updates the quantity of the specified product
    to the specified amount
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(
            request, f'Updated {product.name} quantity in your basket')
    else:
        basket.pop(item_id)
        messages.success(
            request, f'Removed {product.name} from your basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """
    Removes the item from the shopping bag
    """
    product = get_object_or_404(Product, pk=item_id)
    try:
        basket = request.session.get('basket', {})
        basket.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')
        request.session['basket'] = basket
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(
            request, f'The item has not been removed - an error occurred: {e}')
        return HttpResponse(status=500)
