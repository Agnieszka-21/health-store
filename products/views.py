from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponse
from .models import Category, Brand, Product, Image


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    images = Image.objects.all()
    all_categories = Category.objects.all()
    all_brands = Brand.objects.all()
    query = None
    categories = None
    brands = None
    # sort = None
    # direction = None
    # current_sorting = f'{sort}_{direction}'

    if request.method == "GET":
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            print('Products: ', products)
            categories = Category.objects.filter(name__in=categories)
            print('Categories: ', categories)

        if 'brand' in request.GET:
            brands = request.GET['brand'].split(',')
            products = products.filter(brand__name__in=brands)
            print('Products: ', products)
            brands = Brand.objects.filter(name__in=brands)
            print('Brands: ', brands)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'Please enter a keyword to find a product')
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(ingredients__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'images': images,
        'all_brands': all_brands,
        'current_brands': brands,
        'all_categories': all_categories,
        'current_categories': categories,
        'search_term': query,
        # 'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    product_images = Image.objects.filter(product=product)
    print(product_images)

    context = {
        'product': product,
        'product_images': product_images,
    }

    return render(request, 'products/product_detail.html', context)
