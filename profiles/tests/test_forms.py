from django.test import SimpleTestCase

from ..forms import UserProfileForm


class UserProfileFormTest(SimpleTestCase):

    def test_form_model(self):
        """
        Tests which model is used by this form
        """
        form = UserProfileForm()
        self.assertTrue(form.Meta.model, 'UserProfile')

    def test_user_field_is_excluded(self):
        """
        Tests whether the model field 'user' is excluded
        """
        form = UserProfileForm()
        self.assertEqual(form.Meta.exclude, ('user',))

    def test_phone_number_autofocus(self):
        """
        Tests autofocus on the field 'default_phone_number'
        """
        form = UserProfileForm()
        self.assertTrue(
            form.fields['default_phone_number'].widget.attrs['autofocus'])
