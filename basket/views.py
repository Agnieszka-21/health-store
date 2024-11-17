from django.shortcuts import render, HttpResponse


# Create your views here.

def view_basket(request):
    """ A view that renders the bag contents page """
    return HttpResponse('This is the page for your basket')
