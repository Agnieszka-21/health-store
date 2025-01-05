from django.test import SimpleTestCase

from ..forms import UserProfileForm


class UserProfileFormTest(SimpleTestCase):

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
        self.assertTrue(form.fields['default_phone_number'].widget.attrs['autofocus'] == True)

    # def test_full_name_is_required(self):
    #     form = UserProfileForm()
    #     self.assertTrue(form.fields['default_full_name'].required)

        # def test_placeholder_for_required_fields(self):
    #     form = UserProfileForm()
    #     # self.assertTrue(
    #     for field in form.fields:
    #         if form.fields[field].required:
    #             placeholder = f'{placeholders[field]} *'

    #     self.assertTrue(form.fields[field].data[placeholder] == f'{placeholders[field]} *')





