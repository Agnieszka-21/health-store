from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models.functions import Lower

from bs4 import BeautifulSoup

from .models import Category, Brand, Product, Image, Wishlist, Review
from .forms import ProductForm, ImageForm, ReviewForm


def all_products(request):
    """ Show all products, including sorting and search queries """

    products = Product.objects.all()
    all_categories = Category.objects.all()
    all_brands = Brand.objects.all()
    query = None
    categories = None
    brands = None
        
    sort = None
    direction = None

    if request.method == "GET":
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

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

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'all_brands': all_brands,
        'current_brands': brands,
        'all_categories': all_categories,
        'current_categories': categories,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


# @login_required
# def handle_rating(request, product_id):
#     if request.POST and 'rating_id' in request.POST:
#         print('Star rating - ajax post request')
#         print('rating_id: ', request.POST['rating_id'])
#         if request.POST['rating_id'] == 'star1':
#             star_rating = 1
#         elif request.POST['rating_id'] == 'star2':
#             star_rating = 2
#         elif request.POST['rating_id'] == 'star3':
#             star_rating = 3
#         elif request.POST['rating_id'] == 'star4':
#             star_rating = 4
#         elif request.POST['rating_id'] == 'star5':
#             star_rating = 5
#         return star_rating


def product_detail(request, product_id):
    """ Show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    product_images = Image.objects.filter(product=product)
    reviews = product.reviews.all().order_by("-created_on")
    review_count = product.reviews.filter(approved=True).count()

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        context = {
            'product': product,
            'product_images': product_images,
            'reviews': reviews,
            'review_count': review_count,
            'review_form': review_form,
        }

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.product = product
            review.rating = request.POST['stars-rating']
            print('Request.POST: ', request.POST['stars-rating'])

            try:
                print('Try block in def product_detail')
                review.save()
                print('Review was saved')
                messages.success(
                    request, 'Thank you! Review submitted and awaiting approval'
                )
            except Exception as e:
                print('Exception:', e)
            return HttpResponseRedirect(reverse('product_detail', args=[product_id]))

    else:
        review_form = ReviewForm()
        context = {
            'product': product,
            'product_images': product_images,
            'reviews': reviews,
            'review_count': review_count,
            'review_form': review_form,
        }

    return render(request, 'products/product_detail.html', context)


@login_required
def edit_review(request, product_id, review_id):
    """
    Edit a review
    """
    if request.method == "POST":
        product = get_object_or_404(Product, pk=product_id)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.author == request.user:
            review = review_form.save(commit=False)
            review.product = product
            review.approved = False
            review.save()
            messages.success(request, 'Your review has been updated!')
        else:
            messages.error(request, 'Error updating review!')

    return HttpResponseRedirect(reverse('product_detail', args=[product_id]))


@login_required
def delete_review(request, product_id, review_id):
    """
    view to delete review
    """
    product = get_object_or_404(Product, pk=product_id)
    review = get_object_or_404(Review, pk=review_id)

    if review.author == request.user:
        review.delete()
        messages.success(request, 'Review deleted!')
    else:
        messages.error(request, 'You can only delete your own reviews!')

    return HttpResponseRedirect(reverse('product_detail', args=[product_id]))


@login_required
def add_to_wishlist(request, product_id):

    if request.POST and 'attr_id' in request.POST:
        print('Add to wishlist - ajax post request')
        print('attr_id: ', request.POST['attr_id'])
        print('icon_classlist_value: ', request.POST['icon_classlist_value'])

        wishlist = Wishlist.objects.get(user_profile = request.user.profile)
        print('Wishlist: ', wishlist)

        if 'fa-regular' in request.POST['icon_classlist_value']:
            wishlist.favourite_products.add(request.POST['attr_id'])
        elif 'fa-solid' in request.POST['icon_classlist_value']:
            wishlist.favourite_products.remove(request.POST['attr_id'])

        print('Wishlist updated - products: ', wishlist.favourite_products.all())

    else:
        messages.error(request, 'Sorry, something went wrong')
        print('Sorry, something went wrong')

    return redirect(reverse('products'))


@login_required
def remove_from_wishlist(request, product_id):

    if request.POST and 'attr_id' in request.POST:
        print('Remove from wishlist - ajax post request')
        print('attr_id: ', request.POST['attr_id'])

        wishlist = Wishlist.objects.get(user_profile = request.user.profile)
        print('Wishlist: ', wishlist)

        wishlist.favourite_products.remove(request.POST['attr_id'])
        updated_wishlist = wishlist.favourite_products.all()
        wishlist_items = updated_wishlist

        print('Wishlist items: ', wishlist_items)
        return render(request, 'profiles/profile.html', {'wishlist_items': wishlist_items})

    else:
        messages.error(request, 'Sorry, something went wrong')
        print('Sorry, something went wrong')

    return render(request, 'profiles/profile.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity in your basket')
    else:
        basket[item_id] = quantity
        messages.success(request, f'Added {product.name} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


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
                if added_images.primary_img:
                    added_images.product = added_product
                    added_images.name_primary_img = f'{added_product.name } main image'
                    if added_images.secondary_img:
                        added_images.name_secondary_img = f'{added_product.name } additional image 1'
                        if added_images.tertiary_img:
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
    product_images = Image.objects.filter(product=product)

    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES, instance=product)
        if product_images:
            existing_product_img = Image.objects.get(product=product)
            image_form = ImageForm(request.POST, request.FILES, instance=existing_product_img)
        else:
            image_form = ImageForm(request.POST, request.FILES)

        if product_form.is_valid():
            edited_product = product_form.save()

            if image_form.is_valid():
                edited_images = image_form.save(commit=False)
                if edited_images.primary_img:
                    edited_images.product = edited_product
                    edited_images.name_primary_img = f'{edited_product.name } main image'
                    if edited_images.secondary_img:
                        edited_images.name_secondary_img = f'{edited_product.name } additional image 1'
                        if edited_images.tertiary_img:
                            edited_images.name_tertiary_img = f'{edited_product.name} additional image 2'
                    edited_images.save()
                else:
                    messages.error(request, 'A primary image is required if you want to add a secondary image. A secondary image is required if you want to add a tertiary image')
                    return redirect(reverse('edit_product', args=[edited_product.id]))

                messages.success(request, 'Successfully updated product!')
                return redirect(reverse('product_detail', args=[edited_product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        product_form = ProductForm(instance=product)
        if product_images:
            existing_product_img = Image.objects.get(product=product)
            image_form = ImageForm(instance=existing_product_img)
        else:
            image_form = ImageForm()

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

    if request.method == 'POST':
        try:
            product.delete()
            messages.success(request, 'Product deleted!')
            return redirect(reverse('products'))
        except Exception:
            messages.error(request, 'Sorry, the product could not be deleted')

    template = 'products/delete_product.html'
    context = {'product': product}

    return render(request, template, context)
