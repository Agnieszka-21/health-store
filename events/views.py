from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.utils.timezone import make_aware
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .forms import EventForm
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
        open_for_registration()
        upcoming_events = Event.objects.filter(registration_open=True)
        cancelled = upcoming_events.filter(cancelled=True)
        context['upcoming_events'] = upcoming_events
        context['cancelled'] = cancelled

        return context


def open_for_registration():

    all_events = Event.objects.all()
    current_datetime = datetime.now()
    for event in all_events:
        print('event', event)
        if event.when > make_aware(current_datetime):
            event.registration_open = True
            event.save()
        else:
            event.registration_open = False
            event.save()

        return event


@login_required
def create_event(request):

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins can add an online event.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            added_event = event_form.save()
            messages.success(request, 'Successfully created and saved event!')
            return redirect(reverse('events'))
        else:
            messages.error(request, 'Failed to add event. Please ensure the form is valid.')
    else:
        event_form = EventForm()
        
    template = 'events/create_event.html'
    context = {
        'event_form': event_form,
    }

    return render(request, template, context)


@login_required
def edit_event(request, event_id):
    """ Edit an online event """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins can edit an online event.')
        return redirect(reverse('home'))

    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        event_form = EventForm(request.POST, request.FILES, instance=event)

        if event_form.is_valid():
            edited_event = event_form.save()
            messages.success(request, 'Successfully updated the event')
            return redirect(reverse('events'))
        else:
            messages.error(request, 'Failed to update event. Please ensure the form is valid.')
    else:
        event_form = EventForm(instance=event)
        messages.info(request, f'You are editing {event.title}')

    template = 'events/edit_event.html'
    context = {
        'event_form': event_form,
        'event': event,
    }
    return render(request, template, context)


@login_required
def event_register(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    user = request.user
    print('User: ', user)

    if request.method == 'POST':
        try:
            event.participants.add(user)
            print('Add user')
            event.save()
            print('Event participants: ', event.participants)
            messages.success(request, 'You have been registered')
            send_confirmation_email(user, event)
            print('Email sent')
            return redirect(reverse('events'))
        except Exception as e:
            print('Exception: ', e)
            messages.error(request, 'Sorry, something went wrong. Please try again later.')

    template = 'events/event_registration.html'
    context = {
        'event': event,
    }
    return render(request, template, context)


def send_confirmation_email(user, event):
    """Send the user a confirmation email after they registered for an event"""
    user_email = user.email
    print(user_email)
    subject = render_to_string(
        'events/confirmation_emails/confirmation_email_subject.txt',
    )
    body = render_to_string(
        'events/confirmation_emails/confirmation_email_body.txt',
        {'event': event, 'user': user, 'contact_email': settings.DEFAULT_FROM_EMAIL})
    
    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [user_email]
    )


@login_required
def delete_event(request, event_id):
    """ Delete an online event """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store managers can delete an online event.')
        return redirect(reverse('home'))

    event = get_object_or_404(Event, pk=event_id)

    if request.method == 'POST':
        try:
            event.delete()
            messages.success(request, 'Event deleted!')
            return redirect(reverse('events'))
        except Exception:
            messages.error(request, 'Sorry, the event could not be deleted')

    template = 'events/delete_event.html'
    context = {'event': event}

    return render(request, template, context)
