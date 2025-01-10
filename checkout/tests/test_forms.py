from django.test import SimpleTestCase

from ..forms import OrderForm


class OrderFormTest(SimpleTestCase):

    def test_form_model(self):
        """
        Tests the model for this form
        """
        form = OrderForm()
        self.assertTrue(form.Meta.model, 'Order')

    def test_form_fields(self):
        """
        Tests which fields are included in this form
        """
        form = OrderForm()
        self.assertTrue(form.Meta.fields, (
            'full_name', 'email', 'phone_number',
            'street_address1', 'street_address2',
            'town_or_city', 'county', 'postcode', 'country',))

    def test_full_name_autofocus(self):
        """
        Tests the 'autofocus' attribute on the field 'full_name'
        """
        form = OrderForm()
        self.assertTrue(
            form.fields['full_name'].widget.attrs['autofocus'])

    def test_required_field_placeholder(self):
        """
        Tests the placeholder for a required field like 'full_name'
        """
        form = OrderForm()
        self.assertEqual(
            form.fields['full_name'].widget.attrs['placeholder'],
            'Full Name *')

    def test_not_required_field_placeholder(self):
        """
        Tests the placeholder for a non-required field like 'street_address2'
        """
        form = OrderForm()
        self.assertEqual(
            form.fields['street_address2'].widget.attrs['placeholder'],
            'Street Address 2')

    def test_fields_widget_class(self):
        """
        Tests the class set for the field 'full_name'
        """
        form = OrderForm()
        self.assertEqual(
            form.fields['full_name'].widget.attrs['class'],
            'stripe-style-input')

    def test_fields_label(self):
        """
        Tests the absence of field labels - field 'full_name'
        used as an example
        """
        form = OrderForm()
        self.assertFalse(form.fields['full_name'].label)
