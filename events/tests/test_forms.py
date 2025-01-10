from django.test import SimpleTestCase, TestCase

from ..forms import EventForm


class EventFormTest(SimpleTestCase):

    def test_form_model(self):
        """
        Tests the model for this form
        """
        form = EventForm()
        self.assertTrue(form.Meta.model, 'Event')

    def test_form_fields(self):
        """
        Tests which fields are included in this form
        """
        form = EventForm()
        self.assertTrue(form.Meta.fields, [
            'title',
            'when',
            'speaker',
            'description',
            'cancelled',
        ])

    def test_field_when_placeholder(self):
        """
        Tests the placeholder of the field 'when'
        """
        form = EventForm()
        self.assertTrue(
            form.fields['when'].widget.attrs['placeholder'] == (
                'yyyy-mm-dd hh:mm:ss'))
