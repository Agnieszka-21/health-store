from django.test import SimpleTestCase

from ..forms import CarouselForm


class CarouselFormTest(SimpleTestCase):

    def test_display_field_is_excluded(self):
        """
        Tests whether the model field 'display' is excluded
        """
        form = CarouselForm()
        self.assertEqual(form.Meta.exclude, ('display',))

    def test_title_is_required(self):
        """
        Tests whether the field 'title' is required
        """
        form = CarouselForm()
        self.assertTrue(form.fields['title'].required)

    def test_banner_img1_is_required(self):
        """
        Tests whether the field 'banner_img1' is required
        """
        form = CarouselForm()
        self.assertTrue(form.fields['banner_img1'].required)

    def test_banner_img2_is_required(self):
        """
        Tests whether the field 'banner_img2' is required
        """
        form = CarouselForm()
        self.assertTrue(form.fields['banner_img2'].required)

    def test_banner_img3_is_required(self):
        """
        Tests whether the field 'banner_img3' is required
        """
        form = CarouselForm()
        self.assertTrue(form.fields['banner_img3'].required)

    def test_banner_img4_is_required(self):
        """
        Tests whether the field 'banner_img4' is required
        """
        form = CarouselForm()
        self.assertTrue(form.fields['banner_img4'].required)
