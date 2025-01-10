from django.test import SimpleTestCase, TestCase
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from ..forms import ProductForm, ImageForm, ReviewForm
from ..models import Category


class ProductFormTest(TestCase):

    def test_form_model(self):
        """
        Tests the model for this form
        """
        form = ProductForm()
        self.assertTrue(form.Meta.model, 'Product')

    def test_category_choices_are_friendly_names(self):
        """
        Tests whether category choices are friendly names
        """
        form = ProductForm()
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.assertTrue(form.fields['category'].choices == friendly_names)


class ImageFormTest(SimpleTestCase):

    def test_form_model(self):
        """
        Tests which model is used by this form
        """
        form = ImageForm()
        self.assertTrue(form.Meta.model, 'Image')

    def test_primary_img_not_required(self):
        """
        Tests whether the field 'primary_img' is required
        """
        form = ImageForm()
        self.assertFalse(form.fields['primary_img'].required)

    def test_secondary_img_not_required(self):
        """
        Tests whether the field 'secondary_img' is required
        """
        form = ImageForm()
        self.assertFalse(form.fields['secondary_img'].required)

    def test_tertiary_img_not_required(self):
        """
        Tests whether the field 'tertiary_img' is required
        """
        form = ImageForm()
        self.assertFalse(form.fields['tertiary_img'].required)

    def test_primary_img_help_text(self):
        """
        Tests help text for the field 'primary_img'
        """
        form = ImageForm()
        primary_help = mark_safe(_(
                '<small style="color:red">Please be advised that if you \
                delete (clear) your custom primary image and do not provide \
                a replacement, all images for this product will be \
                permanently deleted.</small>'))
        self.assertTrue(form.fields['primary_img'].help_text == primary_help)


class ReviewFormTest(SimpleTestCase):

    def test_form_model(self):
        """
        Tests which model is used by this form
        """
        form = ReviewForm()
        self.assertTrue(form.Meta.model, 'Review')

    def test_form_fields(self):
        """
        Tests the fields included in this form
        """
        form = ReviewForm()
        self.assertTrue(form.Meta.fields, ['text'])
