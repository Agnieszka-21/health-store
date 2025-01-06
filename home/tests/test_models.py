from django.test import TestCase

from ..models import Carousel


class CarouselModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Sets up non-modified objects used by all test methods
        """
        Carousel.objects.create(title='Test carousel')

    def test_title_label(self):
        """
        Tests the label of the title field
        """
        carousel = Carousel.objects.get(id=1)
        field_label = carousel._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_banner_img1_label(self):
        """
        Tests the label of the banner_img1 field
        """
        carousel = Carousel.objects.get(id=1)
        field_label = carousel._meta.get_field('banner_img1').verbose_name
        self.assertEqual(field_label, 'banner img1')

    def test_name_banner_img1_label(self):
        """
        Tests the label of the name_banner_img1 field
        """
        carousel = Carousel.objects.get(id=1)
        field_label = carousel._meta.get_field('name_banner_img1').verbose_name
        self.assertEqual(field_label, 'name banner img1')

    def test_banner_img2_label(self):
        """
        Tests the label of the banner_img2 field
        """
        carousel = Carousel.objects.get(id=1)
        field_label = carousel._meta.get_field('banner_img2').verbose_name
        self.assertEqual(field_label, 'banner img2')

    def test_name_banner_img2_label(self):
        """
        Tests the label of the name_banner_img2 field
        """
        carousel = Carousel.objects.get(id=1)
        field_label = carousel._meta.get_field('name_banner_img2').verbose_name
        self.assertEqual(field_label, 'name banner img2')

    def test_banner_img3_label(self):
        """
        Tests the label of the banner_img3 field
        """
        carousel = Carousel.objects.get(id=1)
        field_label = carousel._meta.get_field('banner_img3').verbose_name
        self.assertEqual(field_label, 'banner img3')

    def test_name_banner_img3_label(self):
        """
        Tests the label of the name_banner_img3 field
        """
        carousel = Carousel.objects.get(id=1)
        field_label = carousel._meta.get_field('name_banner_img3').verbose_name
        self.assertEqual(field_label, 'name banner img3')

    def test_banner_img4_label(self):
        """
        Tests the label of the banner_img4 field
        """
        carousel = Carousel.objects.get(id=1)
        field_label = carousel._meta.get_field('banner_img4').verbose_name
        self.assertEqual(field_label, 'banner img4')

    def test_name_banner_img4_label(self):
        """
        Tests the label of the name_banner_img4 field
        """
        carousel = Carousel.objects.get(id=1)
        field_label = carousel._meta.get_field('name_banner_img4').verbose_name
        self.assertEqual(field_label, 'name banner img4')

    def test_title_max_length(self):
        """
        Tests the maximum length of the title field
        """
        carousel = Carousel.objects.get(id=1)
        max_length = carousel._meta.get_field('title').max_length
        self.assertEqual(max_length, 254)

    def test_name_banner_img1_max_length(self):
        """
        Tests the maximum length of the name_banner_img1 field
        """
        carousel = Carousel.objects.get(id=1)
        max_length = carousel._meta.get_field('name_banner_img1').max_length
        self.assertEqual(max_length, 254)

    def test_name_banner_img2_max_length(self):
        """
        Tests the maximum length of the name_banner_img2 field
        """
        carousel = Carousel.objects.get(id=1)
        max_length = carousel._meta.get_field('name_banner_img2').max_length
        self.assertEqual(max_length, 254)

    def test_name_banner_img3_max_length(self):
        """
        Tests the maximum length of the name_banner_img3 field
        """
        carousel = Carousel.objects.get(id=1)
        max_length = carousel._meta.get_field('name_banner_img3').max_length
        self.assertEqual(max_length, 254)

    def test_name_banner_img1_max_length(self):
        """
        Tests the maximum length of the name_banner_img4 field
        """
        carousel = Carousel.objects.get(id=1)
        max_length = carousel._meta.get_field('name_banner_img4').max_length
        self.assertEqual(max_length, 254)

    def test_display_is_false_by_default(self):
        """
        Tests the default value of the display field
        """
        carousel = Carousel.objects.get(id=1)
        display = carousel._meta.get_field('display').default
        self.assertFalse(display, True)

    def test_carousel_ordering(self):
        """
        Tests the ordering of Carousel objects
        """
        carousel = Carousel.objects.get(id=1)
        ordering = carousel._meta.ordering
        self.assertEqual(ordering, ['-created_on'])

    def test_object_name_is_title(self):
        """
        Tests the string representation of the Carousel object
        """
        carousel = Carousel.objects.get(id=1)
        expected_object_name = f'{carousel.title}'
        self.assertEqual(str(carousel), expected_object_name)
