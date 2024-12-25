from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Carousel
from .forms import CarouselForm


def home(request):
    try:
        carousel = Carousel.objects.get(display=True)
    except Exception:
        carousel = get_object_or_404(Carousel, id=1)

    context = {
        'carousel': carousel,
    }
    return render(request, 'home/index.html', context)


@login_required
def choose_carousel(request):
    available_carousels = Carousel.objects.all()
    current_home_carousel = Carousel.objects.get(display=True)
    print('available_carousels: ', available_carousels)
    print('current_home_carousel', current_home_carousel)

    if request.method == "POST":
        try:
            chosen_carousel_title = request.POST['available-carousels']
            print('chosen_carousel_title: ', chosen_carousel_title)
            chosen_carousel = Carousel.objects.get(title=chosen_carousel_title)
            print('chosen_carousel: ', chosen_carousel)
            chosen_carousel.display = True
            chosen_carousel.save()
            current_home_carousel.display = False
            current_home_carousel.save()
            messages.success(request, 'Homepage carousel was successfully updated')
            
            return redirect(reverse('home'))
            
        except Exception:
            messages.success(request, 'Sorry, an error occurred')

    context = {
        'available_carousels': available_carousels,
    }
    template = 'home/choose_carousel.html'
    return render(request, template, context)


@login_required
def create_carousel(request):
    """ Add a carousel for the homepage """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store managers can add a carousel.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        carousel_form = CarouselForm(request.POST, request.FILES)
        if carousel_form.is_valid():
            added_carousel = carousel_form.save()
            messages.success(request, 'Successfully added carousel!')
            return redirect(reverse('home'))

        else:
            messages.error(request, 'Failed to add a new carousel. Please ensure the form is valid.')
    else:
        carousel_form = CarouselForm()
        
    template = 'home/create_carousel.html'
    context = {
        'carousel_form': carousel_form,
    }

    return render(request, template, context)
