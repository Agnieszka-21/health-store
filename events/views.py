from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.template.loader import render_to_string
from django.utils.timezone import make_aware
from django.views.generic.list import ListView
from datetime import datetime

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
    model = Event
    ordering = ['when']
    paginate_by = 5
    template_name = 'events/events.html'

    def get_context_data(self, **kwargs):
        """
        Updates the context by finding upcoming events
        (ones that are open for registration)
        """
        context = super().get_context_data(**kwargs)
        open_for_registration()
        upcoming_events = Event.objects.filter(
            registration_open=True)
        context['upcoming_events'] = upcoming_events

        return context


def open_for_registration():
    """
    Automatically marks an event as open for registration
    if the event starts in the future
    """
    all_events = Event.objects.all()
    current_datetime = datetime.now()
    for event in all_events:
        if event.when > make_aware(current_datetime):
            event.registration_open = True
            event.save()
        else:
            event.registration_open = False
            event.save()
        return event


@login_required
def create_event(request):
    """
    Creates a new online event - for managers only

    **Template:**

    :template:`events/create_event.html`
    """
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
            messages.error(
                request, 'Failed to add event. \
                Please ensure the form is valid.')
    else:
        event_form = EventForm()

    template = 'events/create_event.html'
    context = {'event_form': event_form}

    return render(request, template, context)


@login_required
def edit_event(request, event_id):
    """
    Edits an online event - for managers only

    **Template:**

    :template:`events/edit_event.html`
    """
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
            messages.error(
                request, 'Failed to update event. \
                Please ensure the form is valid.')
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
    """
    Registers an authenticated user to a specific online event

    **Template:**

    :template:`events/event_registration.html`
    """
    event = get_object_or_404(Event, pk=event_id)
    user = request.user

    if request.method == 'POST':
        try:
            event.participants.add(user)
            event.save()
            messages.success(request, 'You have been registered')
            send_confirmation_email(user, event)
            return redirect(reverse('events'))
        except Exception:
            messages.error(
                request, 'Sorry, something went wrong. \
                Please try again later.')

    template = 'events/event_registration.html'
    context = {'event': event}

    return render(request, template, context)


def send_confirmation_email(user, event):
    """
    Sends the user a confirmation email after they
    registered for an event
    """
    user_email = user.email
    print(user_email)
    subject = render_to_string(
        'events/confirmation_emails/confirmation_email_subject.txt',
    )
    body = render_to_string(
        'events/confirmation_emails/confirmation_email_body.txt',
        {
            'event': event,
            'user': user,
            'contact_email': settings.DEFAULT_FROM_EMAIL
        }
    )
    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [user_email]
    )


@login_required
def delete_event(request, event_id):
    """
    Deletes an online event - for managers only

    **Template:**

    :template:`events/delete_event.html`
    """

    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only store managers can delete an online event.')
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
