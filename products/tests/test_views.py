from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from decimal import Decimal

from ..models import Category, Brand, Product, Wishlist, Review


class AllProductsViewTest(TestCase):
    def setUp(self):
        """
        Sets up data for profile view tests
        """
        test_user = User.objects.create_user(
            username='testuser',
            email='testuser@email.com',
            password='1X<12345+tuK',
            is_staff=False,
        )
        test_user.save()

        product1 = Product.objects.create(
            name='Vitamin D',
            price=20.99
        )
        product2 = Product.objects.create(
            name='Bar Soap Lemon',
            price=5.99
        )

    def test_user_can_access_without_logging_in(self):
        """
        Tests whether any user is granted access
        to the page displaying all products
        """
        test_user = User.objects.get(username='testuser')
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """
        Tests whether the url related to this view
        can be accessed by its name
        """
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Tests whether the correct template is used
        """
        response = self.client.get(reverse('products'))
        self.assertTemplateUsed(response, 'products/products.html')

    def test_view_displays_all_products(self):
        product1 = Product.objects.get(name='Vitamin D')
        product2 = Product.objects.get(name='Bar Soap Lemon')
        products = Product.objects.all()
        response = self.client.get(reverse('products'))
        self.assertTrue(response.context['products_number'] == 2)


class ProductDetailViewTest(TestCase):
    def setUp(self):
        """
        Sets up data for profile view tests
        """
        test_user = User.objects.create_user(
            username='testuser',
            email='testuser@email.com',
            password='1X<12345+tuK',
            is_staff=False,
        )
        test_user.save()
        category = Category.objects.create(
            name='supplements',
            friendly_name='Supplements'
        )
        brand = Brand.objects.create(
            name='viridian',
            friendly_name='Viridian'
        )
        product = Product.objects.create(
            category=category,
            brand=brand,
            sku='SKUU001',
            name='Vitamin D',
            description='Supplement for better immunity',
            ingredients='Vitamin D3',
            price=20.99
        )

    def test_user_can_access_without_logging_in(self):
        """
        Tests whether any user is granted access
        to the page displaying all products
        """
        test_user = User.objects.get(username='testuser')
        product = Product.objects.get(id=1)
        response = self.client.get(f'/products/{product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['product'], product)

    def test_view_url_accessible_by_name(self):
        """
        Tests whether the url related to this view
        can be accessed by its name
        """
        product = Product.objects.get(id=1)
        response = self.client.get(
            reverse('product_detail', args=[product.id]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Tests whether the correct template is used
        """
        product = Product.objects.get(id=1)
        response = self.client.get(
            reverse('product_detail', args=[product.id]))
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_view_displays_correct_product(self):
        """
        Tests whether the correct specific product is displayd
        """
        test_user = User.objects.get(username='testuser')
        product = Product.objects.get(id=1)
        response = self.client.get(f'/products/{product.id}/')
        self.assertEqual(
            response.context['product'], product)
        self.assertEqual(
            response.context['product'].name, 'Vitamin D')
        self.assertEqual(
            response.context['product'].price, Decimal('20.99'))
        self.assertEqual(
            response.context['product'].sku, 'SKUU001')
        self.assertEqual(
            response.context['product'].brand.friendly_name, 'Viridian')

    def test_authenticated_user_can_submit_review(self):
        """
        Tests whether an authenticated user can create
        a product review
        """
        test_user = User.objects.get(username='testuser')
        logged_in = self.client.login(
            username='testuser', password='1X<12345+tuK',
        )
        self.assertTrue(logged_in)
        product = Product.objects.get(id=1)
        # Check current number of reviews for this product
        response = self.client.get(reverse(
            'product_detail', args=[product.id]))
        self.assertEqual(response.context['review_count'], 0)
        # Create a new review without text - approved by default
        review = Review.objects.create(
            product=product,
            author=test_user,
            rating=5,
            text='',
            created_on='2024-12-12 12:00:00',
            approved=True,
        )
        review.save()
        response = self.client.get(reverse(
            'product_detail', args=[product.id]))
        self.assertEqual(response.status_code, 200)
        # Check updated number of reviews for this product
        response = self.client.get(reverse(
            'product_detail', args=[product.id]))
        self.assertEqual(response.context['review_count'], 1)


class ProductAdminViewsTest(TestCase):
    def setUp(self):
        """
        Sets up data that can be modified in the methods below
        Used for the following **views:**

        :view:`add_product`
        :view:`edit_product`
        :view:`delete_product`
        """
        test_customer = User.objects.create_user(
            username='testuser',
            email='testuser@email.com',
            password='1X<ISRUkw+tuK',
            is_staff=False,
        )
        test_customer.save()
        test_staffuser = User.objects.create_user(
            username='teststaffuser',
            email='staffuseremail@test.com',
            password='staFF-useR',
            is_staff=True,
        )
        test_staffuser.save()
        test_superuser = User.objects.create_superuser(
            username='testsuperuser',
            email='superuseremail@test.com',
            password='suPeR42315',
            is_superuser=True,
        )
        test_superuser.save()
        self.category = Category.objects.create(
            name='supplements',
            friendly_name='Supplements'
        )
        self.brand = Brand.objects.create(
            name='viridian',
            friendly_name='Viridian'
        )
        self.product = Product.objects.create(
            category=self.category,
            brand=self.brand,
            sku='SKUU001',
            name='Vitamin D',
            description='Supplement for better immunity',
            ingredients='Vitamin D3',
            price=20.99           
        )

    def test_add_unauthenticated_user_redirected(self):
        """
        Tests whether user is redirected if not logged in
        """
        test_staffuser = User.objects.get(username='teststaffuser')
        response = self.client.get(reverse(
            'add_product'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_add_non_staff_user_redirected(self):
        """
        Tests whether unauthenticated user is redirected
        and can not access the page
        """
        test_customer = User.objects.get(username='testuser')
        logged_in = self.client.login(
            username='testuser', password='1X<ISRUkw+tuK',
        )
        self.assertTrue(logged_in)
        self.assertFalse(test_customer.is_staff)
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

    def test_add_staffuser_redirected(self):
        """
        Tests whether authenticated staff user is granted access
        to the event creation page
        """
        test_staffuser = User.objects.get(username='teststaffuser')
        logged_in = self.client.login(
            username='teststaffuser', password='staFF-useR',
        )
        self.assertTrue(logged_in)
        self.assertTrue(test_staffuser.is_staff)
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 302)

    def test_add_superuser_can_access(self):
        """
        Tests whether authenticated supseruser is granted access
        to the event creation page
        """
        test_superuser = User.objects.get(username='testsuperuser')
        logged_in = self.client.login(
            username='testsuperuser', password='suPeR42315',
        )
        self.assertTrue(logged_in)
        self.assertTrue(test_superuser.is_superuser)
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 200)

    def test_add_uses_correct_template(self):
        """
        Tests whether the correct template is used
        when user is logged in
        """
        test_superuser = User.objects.get(username='testsuperuser')
        logged_in = self.client.login(
            username='testsuperuser', password='suPeR42315')
        response = self.client.get(reverse('add_product'))
        self.assertTemplateUsed(response, 'products/add_product.html')

    def test_superuser_can_add_product(self):
        """
        Tests whether logged in superuser can add a new product
        """
        test_superuser = User.objects.get(username='testsuperuser')
        logged_in = self.client.login(
            username='testsuperuser', password='suPeR42315')
        # Check the current number of products on the products page
        response = self.client.get(reverse('products'))
        self.assertTrue(response.context['products_number'] == 1)
        # Create a new product
        new_product = Product.objects.create(
            category=self.category,
            brand=self.brand,
            sku='SKUU002',
            name='Vitamin B12',
            description='Supplement for vegans',
            ingredients='Vitamin B12 from algae',
            price=25.85
        )
        new_product.save()
        response = self.client.post(
            reverse('add_product'))
        self.assertEqual(response.status_code, 200)
        # Check the number of products after adding a new one
        response = self.client.get(reverse('products'))
        self.assertTrue(response.context['products_number'] == 2)

    def test_edit_redirects_if_not_logged_in(self):
        """
        Tests whether user is redirected if not logged in
        """
        test_superuser = User.objects.get(username='testsuperuser')
        response = self.client.get(reverse(
            'edit_product', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)

    def test_edit_staffuser_redirected(self):
        """
        Tests whether an authenticated staff user is redirected
        """
        test_staffuser = User.objects.get(username='teststaffuser')
        response = self.client.get(reverse(
            'edit_product', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)

    def test_edit_superuser_can_access(self):
        """
        Tests whether authenticated supseruser is granted access
        to the edit product page
        """
        test_superuser = User.objects.get(username='testsuperuser')
        logged_in = self.client.login(
            username='testsuperuser', password='suPeR42315',
        )
        self.assertTrue(logged_in)
        self.assertTrue(test_superuser.is_superuser)
        response = self.client.get(reverse(
            'edit_product', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)

    def test_edit_uses_correct_template(self):
        """
        Tests whether the correct template is used
        when user is logged in
        """
        test_superuser = User.objects.get(username='testsuperuser')
        logged_in = self.client.login(
            username='testsuperuser', password='suPeR42315')
        response = self.client.get(reverse(
            'edit_product',
            args=[self.product.id]))
        self.assertTemplateUsed(response, 'products/edit_product.html')

    def test_superuser_can_edit_product(self):
        """
        Tests whether logged in superuser can edit a product
        """
        test_superuser = User.objects.get(username='testsuperuser')
        logged_in = self.client.login(
            username='testsuperuser', password='suPeR42315')
        self.product.name = 'Vitamin D Edited'
        self.product.save()
        response = self.client.post(
            reverse('edit_product', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.product.name, 'Vitamin D Edited')

    def test_delete_unauthenticated_user_redirected(self):
        """
        Tests whether user is redirected if not logged in
        """
        test_superuser = User.objects.get(username='testsuperuser')
        response = self.client.get(reverse(
            'delete_product', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_delete_staffuser_redirected(self):
        """
        Tests whether an authenticated staff user is redirected
        """
        test_staffuser = User.objects.get(username='teststaffuser')
        response = self.client.get(reverse(
            'delete_product', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)

    def test_delete_uses_correct_template(self):
        """
        Tests whether the correct template is used
        when user is logged in
        """
        test_superuser = User.objects.get(username='testsuperuser')
        logged_in = self.client.login(
            username='testsuperuser', password='suPeR42315')
        response = self.client.get(reverse(
            'delete_product',
            args=[self.product.id]))
        self.assertTemplateUsed(response, 'products/delete_product.html')

    def test_superuser_can_delete_event(self):
        """
        Tests whether superuser can delete an event
        """
        test_superuser = User.objects.get(username='testsuperuser')
        logged_in = self.client.login(
            username='testsuperuser', password='suPeR42315')
        response = self.client.post(
            reverse('delete_product', args=[self.product.id]))
        self.product.delete()
        self.assertRedirects(response, reverse('products'))


class ManageReviewsViewTest(TestCase):
    def setUp(self):
        """
        Sets up data that can be modified in the methods below
        Used for the following **views:**

        :view:`add_product`
        :view:`edit_product`
        :view:`delete_product`
        """
        test_user = User.objects.create_user(
            username='testuser',
            email='testuser@email.com',
            password='1X<ISRUkw+tuK',
            is_staff=False,
        )
        test_user.save()
        test_staffuser = User.objects.create_user(
            username='teststaffuser',
            email='staffuseremail@test.com',
            password='staFF-useR',
            is_staff=True,
        )
        test_staffuser.save()
        test_superuser = User.objects.create_superuser(
            username='testsuperuser',
            email='superuseremail@test.com',
            password='suPeR42315',
            is_superuser=True,
        )
        test_superuser.save()
        self.category = Category.objects.create(
            name='supplements',
            friendly_name='Supplements'
        )
        self.brand = Brand.objects.create(
            name='viridian',
            friendly_name='Viridian'
        )
        self.product = Product.objects.create(
            category=self.category,
            brand=self.brand,
            sku='SKUU001',
            name='Vitamin D',
            description='Supplement for better immunity',
            ingredients='Vitamin D3',
            price=20.99           
        )
        review1 = Review.objects.create(
            product=self.product,
            author=test_user,
            rating=5,
            text='Great product',
            created_on='2024-12-12 12:00:00',
        )
        review2 = Review.objects.create(
            product=self.product,
            author=test_staffuser,
            rating=3,
            text='Too pricey',
            created_on='2024-12-10 10:00:00',
        )

    def test_superuser_can_approve_review(self):
        test_superuser = User.objects.get(username='testsuperuser')
        logged_in = self.client.login(
            username='testsuperuser', password='suPeR42315')
        review1 = Review.objects.get(id=1)
        response = self.client.post(
            reverse('manage_reviews'))
        self.assertIn([review1], response.context['new_reviews'])
        # Approve the review  
        review1.approved = True
        review1.save()
        # Check the updated list of new reviews to manage
        response = self.client.post(
            reverse('manage_reviews'))
        self.assertNotIn([review1], response.context['new_reviews']) # FIX
