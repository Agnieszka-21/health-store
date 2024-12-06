from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.

@login_required
def profile(request):
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
