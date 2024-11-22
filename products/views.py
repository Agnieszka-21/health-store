from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Product, Image

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    images = Image.objects.all()
    # query = None
    # categories = None
    # sort = None
    # direction = None

    # current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'images': images,
        # 'search_term': query,
        # 'current_categories': categories,
        # 'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)
