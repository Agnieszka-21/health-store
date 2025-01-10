from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.core import mail
from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import make_aware

from ..models import Event


class DisplayEventsView(TestCase):
    def setUp(self):
        """
        Sets up 3 Event objects
=        """
        event1 = Event.objects.create(
            title='Event 1',
            description='Test description',
            when=make_aware(datetime.now() + timedelta(days=10)),
        )
        event1.save()
        event2 = Event.objects.create(
            title='Event 2',
            description='Test description',
            when=make_aware(datetime.now() + timedelta(days=20)),
        )
        event2.save()
        event3 = Event.objects.create(
            title='Event 3',
            description='Test description',
            when=make_aware(datetime.now() - timedelta(days=30)),
        )
        event3.save()

    def test_view_url_exists_at_desired_location(self):
        """
        Tests whether the url related to this view
        exists at the desired location
        """
        response = self.client.get('/events/')
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        """
        Tests whether the correct template is used
        """
        response = self.client.get('/events/')
        self.assertTemplateUsed('events/events.html')

    def test_view_url_accessible_by_name(self):
        """
        Tests whether the url related to this view
        can be accessed by its name
        """
        response = self.client.get(reverse('events'))
        self.assertEqual(response.status_code, 200)

    def test_lists_all_future_events(self):
        """
        Confirms that the page lists only future events, and does not
        use pagination, so there should be just 2
        """
        response = self.client.get(reverse('events'))
        self.assertEqual(response.status_code, 200)
        self.assertFalse('is_paginated' in response.context)
        self.assertEqual(len(response.context['upcoming_events']), 2)


class EventAdminViewsTest(TestCase):
    def setUp(self):
        """
        Sets up data that can be modified in the methods below
        Used for the following **views:**

        :view:`create_event`
        :view:`edit_event`
        :view:`delete_event`
        """
        test_customer = User.objects.create_user(
            username='testuser',
            email='testuser@email.com',
            password='1X<ISRUkw+tuK',
            is_staff=False,
        )
        test_customer.save()
        test_staffuser = User.objects.create_user(
            username='teststaffuser',
            email='staffuseremail@test.com',
            password='staFF-useR',
            is_staff=True,
        )
        test_staffuser.save()
        test_superuser = User.objects.create_superuser(
            username='testsuperuser',
            email='superuseremail@test.com',
            password='suPeR42315',
            is_superuser=True,
        )
        test_superuser.save()

        self.event = Event.objects.create(
            title='Test Event',
            description='Test description here',
            speaker='Dr Jane Goodall',
            when=make_aware(datetime.now() + timedelta(days=50)),
        )

    def test_create_unauthenticated_user_redirected(self):
        """
        Tests whether user is redirected if not logged in
        """
        test_staffuser = User.objects.get(username='teststaffuser')
        response = self.client.get(reverse(
            'create_event'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_create_non_staff_user_redirected(self):
        """
        Tests whether unauthenticated user is redirected
        and can not access the page
        """
        test_customer = User.objects.get(username='testuser')
        logged_in = self.client.login(
            username='testuser', password='1X<ISRUkw+tuK',
        )
        self.assertTrue(logged_in)
        self.assertFalse(test_customer.is_staff)
        response = self.client.get('/events/create/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

    def test_create_staffuser_redirected(self):
        """
        Tests whether authenticated staff who is not a superuser
        gets redirected and cannot access the event creation page
        """
        test_staffuser = User.objects.get(username='teststaffuser')
        logged_in = self.client.login(
            username='teststaffuser', password='staFF-useR',
        )
        self.assertTrue(logged_in)
        self.assertTrue(test_staffuser.is_staff)
        response = self.client.get('/events/create/')
        self.assertEqual(response.status_code, 302)

    def test_create_superuser_can_access(self):
        """
        Tests whether authenticated supseruser is granted access
        to the event creation page
        """
        test_staffuser = User.objects.get(username='testsuperuser')
        logged_in = self.client.login(
            username='testsuperuser', password='suPeR42315',
        )
        self.assertTrue(logged_in)
        self.assertTrue(test_staffuser.is_superuser)
        response = self.client.get('/events/create/')
        self.assertEqual(response.status_code, 200)

    def test_create_uses_correct_template(self):
        """
        Tests whether the correct template is used
        when user is logged in
        """
        test_superuser = User.objects.get(username='testsuperuser')
        logged_in = self.client.login(
            username='testsuperuser', password='suPeR42315')
        self.assertTrue(logged_in)
        response = self.client.get(reverse('create_event'))
        self.assertTemplateUsed(response, 'events/create_event.html')

    def test_edit_redirects_if_not_logged_in(self):
        """
        Tests whether user is redirected if not logged in
        """
        test_superuser = User.objects.get(username='testsuperuser')
        response = self.client.get(reverse(
            'edit_event', args=[self.event.id]))
        self.assertEqual(response.status_code, 302)

    def test_edit_staffuser_redirected(self):
        """
        Tests whether an authenticated staff user is redirected
        """
        test_staffuser = User.objects.get(username='teststaffuser')
        response = self.client.get(reverse(
            'edit_event', args=[self.event.id]))
        self.assertEqual(response.status_code, 302)

    def test_edit_superuser_can_access(self):
        """
        Tests whether authenticated supseruser is granted access
        to the edit event page
        """
        test_staffuser = User.objects.get(username='testsuperuser')
        logged_in = self.client.login(
            username='testsuperuser', password='suPeR42315',
        )
        self.assertTrue(logged_in)
        self.assertTrue(test_staffuser.is_superuser)
        response = self.client.get(reverse(
            'edit_event', args=[self.event.id]))
        self.assertEqual(response.status_code, 200)

    def test_edit_url_accessible_by_name(self):
        """
        Tests whether the url related to this view
        can be accessed by its name
        """
        test_superuser = User.objects.get(username='testsuperuser')
        logged_in = self.client.login(
            username='testsuperuser', password='suPeR42315')
        response = self.client.get(
            reverse('edit_event', args=[self.event.id]))
        self.assertEqual(response.status_code, 200)

    def test_edit_uses_correct_template(self):
        """
        Tests whether the correct template is used
        when superuser is logged in
        """
        test_superuser = User.objects.get(username='testsuperuser')
        logged_in = self.client.login(
            username='testsuperuser', password='suPeR42315')
        self.assertTrue(logged_in)
        response = self.client.get(reverse(
            'edit_event',
            args=[self.event.id]))
        self.assertTemplateUsed(response, 'events/edit_event.html')

    def test_delete_unauthenticated_user_redirected(self):
        """
        Tests whether user is redirected if not logged in
        """
        test_superuser = User.objects.get(username='testsuperuser')
        response = self.client.get(reverse(
            'delete_event', args=[self.event.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_delete_staffuser_redirected(self):
        """
        Tests whether an authenticated staff user is redirected
        """
        test_staffuser = User.objects.get(username='teststaffuser')
        response = self.client.get(reverse(
            'delete_event', args=[self.event.id]))
        self.assertEqual(response.status_code, 302)

    def test_delete_uses_correct_template(self):
        """
        Tests whether the correct template is used
        when superuser is logged in
        """
        test_superuser = User.objects.get(username='testsuperuser')
        logged_in = self.client.login(
            username='testsuperuser', password='suPeR42315')
        response = self.client.get(reverse(
            'delete_event',
            args=[self.event.id]))
        self.assertTemplateUsed(response, 'events/delete_event.html')

    def test_delete_url_accessible_by_name(self):
        """
        Tests whether the url related to this view
        can be accessed by its name
        """
        test_superuser = User.objects.get(username='testsuperuser')
        logged_in = self.client.login(
            username='testsuperuser', password='suPeR42315')
        response = self.client.get(
            reverse('delete_event', args=[self.event.id]))
        self.assertEqual(response.status_code, 200)

    def test_superuser_can_delete_event(self):
        """
        Tests whether superuser can delete an event
        """
        test_superuser = User.objects.get(username='testsuperuser')
        logged_in = self.client.login(
            username='testsuperuser', password='suPeR42315')
        response = self.client.post(
            reverse('delete_event', args=[self.event.id]))
        self.assertRedirects(response, reverse('events'))


class EventRegisterViewTest(TestCase):
    def setUp(self):
        """
        Sets up data for the event register view tests
        """

        self.event = Event.objects.create(
            title='Test Event',
            description='Test description here',
            speaker='Dr Jane Goodall',
            when=make_aware(datetime.now() + timedelta(days=10)),
        )
        test_user = User.objects.create_user(
            username='testuser',
            email='testuser@email.com',
            password='1X<ISRUkw+tuK',
            is_staff=False,
        )
        test_user.save()

    def test_unauthenticated_user_redirected(self):
        """
        Tests whether an authenticated user is redirected
        """
        test_user = User.objects.get(username='testuser')
        response = self.client.get(reverse(
            'event_register', args=[self.event.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_authenticated_user_can_access(self):
        """
        Tests whether an authenticated user can access
        the registration page and if the correct template
        is used
        """
        test_user = User.objects.get(username='testuser')
        logged_in = self.client.login(
            username='testuser', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse(
            'event_register', args=[self.event.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'events/event_registration.html')

    def test_authenticated_user_can_register(self):
        """
        Tests whether an authenticated user can register for
        an event
        """
        test_user = User.objects.get(username='testuser')
        logged_in = self.client.login(
            username='testuser', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse(
            'event_register', args=[self.event.id]))
        self.event.participants.add(test_user)
        self.event.save()
        self.assertTrue(test_user in self.event.participants.all())
        self.assertEqual(response.status_code, 200)


class SendConfirmationEmailViewTest(TestCase):

    def test_send_email(self):
        """
        Tests if the view sends a confirmation email to
        anyone who registers for an online event
        """
        mail.send_mail(
            'Email subject',
            'Email content',
            'from@healthstore.com',
            ['to@customer.com'],
            fail_silently=False,
        )
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Email subject')
