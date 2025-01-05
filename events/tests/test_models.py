from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Event


class EventModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Sets up non-modified Event object
        used by all test methods
        """
        event1 = Event.objects.create(
            title='Test Event Title',
            when='2028-12-12 20:00:00'
        )

        event2 = Event.objects.create(
            title='Test Event Two Title',
            when='2028-12-20 20:00:00',
            cancelled=True
        )

    def test_title_max_length(self):
        """
        Tests the maximum length of the field 'title'
        """
        event = Event.objects.get(id=1)
        max_length = event._meta.get_field('title').max_length
        self.assertEqual(max_length, 254)

    def test_speaker_max_length(self):
        """
        Tests the maximum length of the field 'speaker'
        """
        event = Event.objects.get(id=1)
        max_length = event._meta.get_field('speaker').max_length
        self.assertEqual(max_length, 254)

    def test_registration_open_is_false_by_default(self):
        """
        Tests whether the value of the field 'registration_open'
        is False by default
        """
        event = Event.objects.get(id=1)
        self.assertFalse(event.registration_open)

    def test_cancelled_is_false_by_default(self):
        """
        Tests whether the value of the field 'cancelled'
        is False by default
        """
        event = Event.objects.get(id=1)
        self.assertFalse(event.cancelled)

    def test_events_ordering(self):
        """
        Tests the ordering of Event objects
        """
        event = Event.objects.get(id=1)
        ordering = event._meta.ordering
        self.assertEqual(ordering, ['-when'])

    def test_str_representation_if_not_cancelled(self):
        """
        Tests string representation if an Event object
        is not marked as cancelled
        """
        event = Event.objects.get(id=1)
        expected_str = f"{event.when} | {event.title}"
        self.assertEqual(str(event), expected_str)

    def test_str_representation_if_not_cancelled(self):
        """
        Tests string representation if an Event object
        is not marked as cancelled
        """
        event = Event.objects.get(id=2)
        expected_str = f"CANCELLED: {event.when} | {event.title}"
        self.assertEqual(str(event), expected_str)
