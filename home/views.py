from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Carousel
from .forms import CarouselForm


def home(request):
    """
    Renders index template and displays a specific
    carousel, if chosen

    **Template:**

    :template:`home/index.html`
    """
    try:
        carousel = Carousel.objects.get(display=True)
    except Exception:
        carousel = None

    context = {
        'carousel': carousel,
    }
    return render(request, 'home/index.html', context)


@login_required
def admin_panel(request):
    """
    Renders the admin panel template

    **Template:**

    :template:`home/admin_panel.html`
    """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only store managers can access Admin Panel')
        return redirect(reverse('home'))

    return render(request, 'home/admin_panel.html')


@login_required
def choose_carousel(request):
    """
    Handles which carousel is displayed on the homepage
    if user chooses Activate Carousel option,
    leads to further templates if user chooses Edit or Delete,

    **Template:**

    :template:`home/choose_carousel.html`
    """

    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only store managers can choose a carousel.')
        return redirect(reverse('home'))

    available_carousels = Carousel.objects.all()
    current_home_carousel = Carousel.objects.get(display=True)

    if request.method == "POST":
        chosen_carousel_title = request.POST['available-carousels']
        chosen_carousel = Carousel.objects.get(title=chosen_carousel_title)
        carousel_id = chosen_carousel.id

        if 'edit_carousel' in request.POST:
            if chosen_carousel_title == 'Default carousel':
                messages.error(
                    request, 'Sorry, the default carousel cannot be edited')
            else:
                return redirect(reverse('edit_carousel', args=[carousel_id]))

        elif 'delete_carousel' in request.POST:
            if chosen_carousel_title == 'Default carousel':
                messages.error(
                    request, 'Sorry, the default carousel cannot be deleted')
            else:
                return redirect(reverse('delete_carousel', args=[carousel_id]))

        elif 'activate_carousel' in request.POST:
            try:
                chosen_carousel.display = True
                chosen_carousel.save()
                current_home_carousel.display = False
                current_home_carousel.save()
                messages.success(
                    request, 'Homepage carousel was successfully updated')
                return redirect(reverse('home'))

            except Exception:
                messages.success(request, 'Sorry, an error occurred')

    context = {'available_carousels': available_carousels}
    template = 'home/choose_carousel.html'
    return render(request, template, context)


@login_required
def delete_carousel(request, carousel_id):
    """
    Deletes a specified carousel - for managers only

    **Template:**

    :template:`home/delete_carousel.html`
    """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only store managers can delete a carousel.')
        return redirect(reverse('home'))

    carousel = get_object_or_404(Carousel, id=carousel_id)

    if request.method == 'POST':
        try:
            carousel.delete()
            messages.success(request, 'Carousel deleted!')
            return redirect(reverse('admin_panel'))
        except Exception:
            messages.error(request, 'Sorry, the carousel could not be deleted')
    context = {'carousel': carousel}
    template = 'home/delete_carousel.html'

    return render(request, template, context)


@login_required
def edit_carousel(request, carousel_id):
    """
    Edits a specified carousel - for managers only

    **Template:**

    :template:`home/edit_carousel.html`
    """

    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only store managers can edit a carousel.')
        return redirect(reverse('home'))

    carousel = get_object_or_404(Carousel, id=carousel_id)

    if request.method == 'POST':
        carousel_form = CarouselForm(
            request.POST, request.FILES, instance=carousel)
        if carousel_form.is_valid():
            edited_carousel = carousel_form.save()
            messages.success(request, 'Successfully edited carousel!')
            return redirect(reverse('admin_panel'))
        else:
            messages.error(
                request, 'Failed to edit the carousel. \
                Please ensure the form is valid.')

    carousel_form = CarouselForm(instance=carousel)
    context = {
        'carousel': carousel,
        'carousel_form': carousel_form,
    }
    template = 'home/edit_carousel.html'

    return render(request, template, context)


@login_required
def create_carousel(request):
    """
    Adds a new carousel - for managers only

    **Template:**

    :template:`home/create_carousel.html`
    """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only store managers can add a carousel.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        carousel_form = CarouselForm(request.POST, request.FILES)
        if carousel_form.is_valid():
            added_carousel = carousel_form.save()
            messages.success(request, 'Successfully added carousel!')
            return redirect(reverse('admin_panel'))
        else:
            messages.error(
                request, 'Failed to add a new carousel. \
                Please ensure the form is valid.')
    else:
        carousel_form = CarouselForm()

    template = 'home/create_carousel.html'
    context = {'carousel_form': carousel_form}

    return render(request, template, context)
