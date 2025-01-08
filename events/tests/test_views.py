from django.contrib.auth.models import User
from datetime import date, timedelta 
from django.test import TestCase
from django.urls import reverse

from ..models import Event


class DisplayEventsView(TestCase):
    def setUp(self):
        today = date.today()
        event1 = Event.objects.create(
            title='Event 1',
            description='Test description',
            when=today + timedelta(days=10),
        )
        event1.save()
        event2 = Event.objects.create(
            title='Event 2',
            description='Test description',
            when=today + timedelta(days=20),
        )
        event2.save()
        event3 = Event.objects.create(
            title='Event 3',
            description='Test description',
            when=today - timedelta(days=30),
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

    def test_lists_all_groupclasses(self):
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

        today = date.today()
        self.event = Event.objects.create(
            title='Test Event',
            description='Test description here',
            speaker='Dr Jane Goodall',
            when=today + timedelta(days=50),
        )

    def test_create_unauthenticated_user_redirected(self):
        """
        Tests whether user is redirected if not logged in
        """
        test_staffuser = User.objects.get(username='teststaffuser')
        response = self.client.get(reverse(
            'create_event'))
        self.assertEqual(response.status_code, 302)

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

    def test_create_staffuser_redirected(self):
        """
        Tests whether authenticated staff user is granted access
        to the event creation page
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
        to the event edit page
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
        when user is logged in
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
        when user is logged in
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
        test_superuser = User.objects.get(username='testsuperuser')
        logged_in = self.client.login(
            username='testsuperuser', password='suPeR42315')
        response = self.client.post(
            reverse('delete_event', args=[self.event.id]))
        self.event.delete()
        self.assertRedirects(response, reverse('events'))
