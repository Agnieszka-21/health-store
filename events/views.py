from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic.list import ListView

from .models import Event


class EventListView(ListView):
    """
    Returns all events in :model:`events.Event`

    **Context**

    ``queryset``
        All  instances of :model:`events.Event`

    **Template:**

    :template:`events/events.html`
    """
    queryset = Event.objects.all()
    template_name = 'events/events.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        upcoming_events = Event.objects.filter()
        context['published_articles'] = published_articles

        return context
