from django.shortcuts import render, HttpResponse


# Create your views here.
def checkout(request):
    return HttpResponse('This is the checkout page')
