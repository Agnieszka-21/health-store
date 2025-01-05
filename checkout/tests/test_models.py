from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Order, OrderLineItem


class OrderModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Sets up non-modified Order object
        used by all test methods
        """
        Order.objects.create(
            order_number='10394734791'
        )

    def test_order_number_max_length(self):
        """
        Tests the maximum length of the field 'order_number'
        """
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('order_number').max_length
        self.assertEqual(max_length, 32)

    def test_full_name_max_length(self):
        """
        Tests the maximum length of the field 'full_name'
        """
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('full_name').max_length
        self.assertEqual(max_length, 50)

    def test_email_max_length(self):
        """
        Tests the maximum length of the field 'email'
        """
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('email').max_length
        self.assertEqual(max_length, 254)

    def test_phone_number_max_length(self):
        """
        Tests the maximum length of the field 'phone_number'
        """
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('phone_number').max_length
        self.assertEqual(max_length, 20)

    def test_postcode_max_length(self):
        """
        Tests the maximum length of the field 'postcode'
        """
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('postcode').max_length
        self.assertEqual(max_length, 20)

    def test_town_or_city_max_length(self):
        """
        Tests the maximum length of the field 'town_or_city'
        """
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('town_or_city').max_length
        self.assertEqual(max_length, 40)

    def test_street_address1_max_length(self):
        """
        Tests the maximum length of the field 'street_address1'
        """
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('street_address1').max_length
        self.assertEqual(max_length, 80)

    def test_delivery_cost_max_digits(self):
        """
        Tests the maximum number of digits of the field 'delivery_cost'
        """
        order = Order.objects.get(id=1)
        max_digits = order._meta.get_field('delivery_cost').max_digits
        self.assertEqual(max_digits, 6)

    def test_delivery_cost_max_digits(self):
        """
        Tests the maximum number of digits of the field 'order_total'
        """
        order = Order.objects.get(id=1)
        max_digits = order._meta.get_field('order_total').max_digits
        self.assertEqual(max_digits, 10)
