from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView

from .forms import UserProfileForm
from .models import UserProfile
from blog.models import Reading, FavouriteRecipe
from checkout.models import Order
from products.models import Wishlist


@login_required
def profile(request):
    """
    Displays the user's profile
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def orders(request):
    """
    Displays user's oder history
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()
    template = 'profiles/orders.html'
    context = {
        'orders': orders
    }
    return render(request, template, context)


def order_history(request, order_number):
    """
    Displays a specific order confirmation from user's oder history
    """
    order = get_object_or_404(Order, order_number=order_number)
    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def wishlist_items(request):
    """
    Display the user's wishlist items
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    wishlist_items = profile.wishlist.favourite_products.all()
    template = 'profiles/wishlist.html'
    context = {
        'wishlist_items': wishlist_items,
    }

    return render(request, template, context)


@login_required
def remove_from_wishlist(request, product_id):
    """
    Removes an item from the user's wishlist
    """
    if request.POST and 'attr_id' in request.POST:

        wishlist = Wishlist.objects.get(user_profile=request.user.profile)
        wishlist.favourite_products.remove(request.POST['attr_id'])
        updated_wishlist = wishlist.favourite_products.all()
        wishlist_items = updated_wishlist
        context = {'wishlist_items': wishlist_items}

        return render(request, 'profiles/profile.html', context)

    else:
        messages.error(request, 'Sorry, something went wrong')

    return render(request, 'profiles/profile.html')


@login_required
def bookmarked(request):
    """
    Displays the user's bookmarked articles and recipes
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    saved_articles = profile.reading_list.bookmarked_articles.all()
    saved_recipes = profile.fav_recipe_list.bookmarked_recipes.all()
    template = 'profiles/bookmarked.html'
    context = {
        'saved_articles': saved_articles,
        'saved_recipes': saved_recipes,
    }

    return render(request, template, context)


@login_required
def remove_article_bookmark(request, article_id):
    """
    Removes an article from the user's reading list
    """
    if request.POST and 'article_id' in request.POST:
        reading_list = Reading.objects.get(user_profile=request.user.profile)
        reading_list.bookmarked_articles.remove(request.POST['article_id'])
        updated_reading_list = reading_list.bookmarked_articles.all()
        saved_articles = updated_reading_list
        context = {'saved_articles': saved_articles}

        return render(request, 'profiles/profile.html', context)

    else:
        messages.error(
            request, 'Sorry, something went wrong with removing \
            article from reading list')

    return render(request, 'profiles/profile.html')


@login_required
def remove_recipe_bookmark(request, recipe_id):
    """
    Removes a recipe from the user's recipe list
    """
    if request.POST and 'recipe_id' in request.POST:
        recipe_list = FavouriteRecipe.objects.get(
            user_profile=request.user.profile)
        recipe_list.bookmarked_recipes.remove(request.POST['recipe_id'])
        updated_recipe_list = recipe_list.bookmarked_recipes.all()
        saved_recipes = updated_recipe_list
        context = {'saved_recipes': saved_recipes}

        return render(request, 'profiles/profile.html', context)

    else:
        messages.error(
            request, 'Sorry, something went wrong with removing \
            recipe from recipe list')

    return render(request, 'profiles/profile.html')
