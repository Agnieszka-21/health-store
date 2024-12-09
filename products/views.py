from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404

from .models import Category, Brand, Product, Image
from .forms import ProductForm, ImageForm


def all_products(request):
    """ Show all products, including sorting and search queries """

    products = Product.objects.all()
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
        'all_brands': all_brands,
        'current_brands': brands,
        'all_categories': all_categories,
        'current_categories': categories,
        'search_term': query,
        # 'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ Show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    product_images = Image.objects.filter(product=product)
    context = {
        'product': product,
        'product_images': product_images,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store managers can add a product.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        image_form = ImageForm(request.POST, request.FILES)

        if product_form.is_valid():
            added_product = product_form.save()
            if image_form.is_valid():
                added_images = image_form.save(commit=False)
                added_images.product = added_product
                added_images.name_primary_img = f'{added_product.name } main image'
                added_images.name_secondary_img = f'{added_product.name } additional image 1'
                added_images.name_tertiary_img = f'{added_product.name} additional image 2'
                added_images.save()
                messages.success(request, 'Successfully added product!')
                return redirect(reverse('product_detail', args=[added_product.id]))
            else:
                messages.error(request, 'Sorry, the form is not valid. Please check your images')
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        product_form = ProductForm()
        image_form = ImageForm()
        
    template = 'products/add_product.html'
    context = {
        'product_form': product_form,
        'image_form': image_form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store managers can edit a product.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES, instance=product)
        image_form = ImageForm(request.POST, request.FILES)
        if product_form.is_valid():
            edited_product = product_form.save()
            if image_form.is_valid():
                edited_images = image_form.save(commit=False)
                edited_images.product = added_product
                edited_images.name_primary_img = f'{edited_product.name } main image'
                edited_images.name_secondary_img = f'{edited_product.name } additional image 1'
                edited_images.name_tertiary_img = f'{edited_product.name} additional image 2'
                edited_images.save()
                messages.success(request, 'Successfully updated product!')
                return redirect(reverse('product_detail', args=[edited_product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        product_form = ProductForm(instance=product)
        image_form = ImageForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'product_form': product_form,
        'image_form': image_form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store managers can delete a product.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
