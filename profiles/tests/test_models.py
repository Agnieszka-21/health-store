from django.contrib.auth.models import User
from django.test import TestCase

from ..models import UserProfile


class UserProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Sets up non-modified objects User and Profile
        used by all test methods
        """
        cls.user = User.objects.create_user(
            id=12345, username='Jack Sparrow'
        )
        cls.profile = cls.user.profile

    def test_full_name_max_length(self):
        """
        Tests the maximum length of the field 'default_full_name'
        """
        profile = UserProfile.objects.get(id=self.profile.id)
        max_length = profile._meta.get_field('default_full_name').max_length
        self.assertEqual(max_length, 40)

    def test_full_name_max_length(self):
        """
        Tests the maximum length of the field 'default_email'
        """
        profile = UserProfile.objects.get(id=self.profile.id)
        max_length = profile._meta.get_field('default_email').max_length
        self.assertEqual(max_length, 30)

    def test_phone_number_max_length(self):
        """
        Tests the maximum length of the field 'default_phone_number'
        """
        profile = UserProfile.objects.get(id=self.profile.id)
        max_length = profile._meta.get_field('default_phone_number').max_length
        self.assertEqual(max_length, 20)

    def test_street_address1_max_length(self):
        """
        Tests the maximum length of the field 'default_street_address1'
        """
        profile = UserProfile.objects.get(id=self.profile.id)
        max_length = profile._meta.get_field('default_street_address1').max_length
        self.assertEqual(max_length, 80)

    def test_postcode_max_length(self):
        """
        Tests the maximum length of the field 'default_postcode'
        """
        profile = UserProfile.objects.get(id=self.profile.id)
        max_length = profile._meta.get_field('default_postcode').max_length
        self.assertEqual(max_length, 20)

    def test_country_blank_label(self):
        """
        Tests the label of the country field
        """
        profile = UserProfile.objects.get(id=1)
        field_label = profile._meta.get_field('default_country').blank_label
        self.assertEqual(field_label, 'Country *')

    def test_str_representation(self):
        """
        Tests the string representation of the Brand object
        """
        profile = UserProfile.objects.get(id=1)
        expected_str_representation = f'{profile.user.username}'
        self.assertEqual(str(profile), expected_str_representation)