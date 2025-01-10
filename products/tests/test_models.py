from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Category, Brand, Product, Review


class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Sets up a non-modified object used by all test methods
        """
        Category.objects.create(
            name='category',
            friendly_name='Category'
        )

    def test_name_label(self):
        """
        Tests the label of the field 'name'
        """
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_friendly_name_label(self):
        """
        Tests the label of the field 'friendly_name'
        """
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('friendly_name').verbose_name
        self.assertEqual(field_label, 'friendly name')

    def test_name_max_length(self):
        """
        Tests the maximum length of the field 'name'
        """
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEqual(max_length, 254)

    def test_friendly_name_max_length(self):
        """
        Tests the maximum length of the field 'name'
        """
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('friendly_name').max_length
        self.assertEqual(max_length, 254)

    def test_category_verbose_name_plural(self):
        """
        Tests the plural verbose name of the Category object that was
        set explicitly since the default version was grammatically
        incorrect
        """
        category = Category.objects.get(id=1)
        verbose_name_plural = category._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, 'Categories')

    def test_str_representation_is_name(self):
        """
        Tests the string representation of the Category object
        """
        category = Category.objects.get(id=1)
        expected_str_representation = f'{category.name}'
        self.assertEqual(str(category), expected_str_representation)


class BrandModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Sets up a non-modified object used by all test methods
        """
        Brand.objects.create(
            name='test_brand',
            friendly_name='Test Brand',
            url='https://google.com'
        )

    def test_name_label(self):
        """
        Tests the label of the field 'name'
        """
        brand = Brand.objects.get(id=1)
        field_label = brand._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_friendly_name_label(self):
        """
        Tests the label of the field 'friendly_name'
        """
        brand = Brand.objects.get(id=1)
        field_label = brand._meta.get_field('friendly_name').verbose_name
        self.assertEqual(field_label, 'friendly name')

    def test_url_label(self):
        """
        Tests the label of the field 'url'
        """
        brand = Brand.objects.get(id=1)
        field_label = brand._meta.get_field('url').verbose_name
        self.assertEqual(field_label, 'url')

    def test_name_max_length(self):
        """
        Tests the maximum length of the field 'name'
        """
        brand = Brand.objects.get(id=1)
        max_length = brand._meta.get_field('name').max_length
        self.assertEqual(max_length, 254)

    def test_friendly_name_max_length(self):
        """
        Tests the maximum length of the field 'friendly_name'
        """
        brand = Brand.objects.get(id=1)
        max_length = brand._meta.get_field('friendly_name').max_length
        self.assertEqual(max_length, 254)

    def test_url_max_length(self):
        """
        Tests the maximum length of the field 'url'
        """
        brand = Brand.objects.get(id=1)
        max_length = brand._meta.get_field('url').max_length
        self.assertEqual(max_length, 180)

    def test_str_representation_is_name(self):
        """
        Tests the string representation of the Brand object
        """
        brand = Brand.objects.get(id=1)
        expected_str_representation = f'{brand.name}'
        self.assertEqual(str(brand), expected_str_representation)

    def test_get_friendly_name(self):
        """
        Tests the method 'get_friendly_name'
        """
        brand = Brand.objects.get(id=1)
        self.assertEqual(brand.get_friendly_name(), 'Test Brand')

    def test_get_url(self):
        """
        Tests the method 'get_url'
        """
        brand = Brand.objects.get(id=1)
        self.assertEqual(brand.get_url(), 'https://google.com')


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Sets up a non-modified object used by all test methods
        """
        cls.category_ = 'supplements'
        cls.category = Category.objects.create(name=cls.category_)
        cls.brand_ = 'Pukka'
        cls.brand = Brand.objects.create(name=cls.brand_)
        cls.product = Product.objects.create(
            category=cls.category,
            brand=cls.brand,
            sku='SKUU001',
            name='SleepEasy Tea',
            description='Supports sleep',
            ingredients='lemon balm, lavender, chamomile',
            price=3.99,
        )

    def test_name_max_length(self):
        """
        Tests the maximum length of the field 'name'
        """
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('name').max_length
        self.assertEqual(max_length, 254)

    def test_sku_max_length(self):
        """
        Tests the maximum length of the field 'sku'
        """
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('sku').max_length
        self.assertEqual(max_length, 254)

    def test_product_ordering(self):
        """
        Tests the ordering of Product objects
        """
        product = Product.objects.get(id=1)
        ordering = product._meta.ordering
        self.assertEqual(ordering, ['name'])

    def test_str_representation_is_name(self):
        """
        Tests the string representation of the Product object
        """
        product = Product.objects.get(id=1)
        expected_str_representation = f'{product.name}'
        self.assertEqual(str(product), expected_str_representation)


class ReviewModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Sets up a non-modified object used by all test methods
        """
        cls.product_ = 'SleepEasy Tea'
        cls.product = Product.objects.create(
            name=cls.product_,
            price=3.99
        )
        cls.author_ = 'User1'
        cls.author = User.objects.create(username=cls.author_)
        cls.review = Review.objects.create(
            product=cls.product,
            author=cls.author,
            rating=5,
            text='review text here',
            created_on='2024-12-12 20:20:20',
            approved=True,
        )

    def test_default_rating(self):
        """
        Tests the default value of the field 'rating'
        """
        review = Review.objects.get(id=1)
        rating = review._meta.get_field('rating').default
        self.assertEqual(rating, 0)

    def test_review_ordering(self):
        """
        Tests the ordering of Review objects
        """
        review = Review.objects.get(id=1)
        ordering = review._meta.ordering
        self.assertEqual(ordering, ['created_on'])

    def test_str_representation(self):
        """
        Tests the string representation of the Review object
        """
        review = Review.objects.get(id=1)
        expected_str_representation = (
            f'Comment {review.text} by {review.author}')
        self.assertEqual(str(review), expected_str_representation)
