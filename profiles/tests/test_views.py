from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from ..models import UserProfile
from checkout.models import Order



class ProfileViewTest(TestCase):
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

        self.profile = test_user.profile

    def test_unauthenticated_user_redirected(self):
        """
        Tests whether user is redirected if not logged in
        """
        test_user = User.objects.get(username='testuser')
        response = self.client.get(reverse(
            'profile'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_authenticated_user_can_access(self):
        """
        Tests whether authenticated user is granted access
        to their profile page
        """
        test_user = User.objects.get(username='testuser')
        logged_in = self.client.login(
            username='testuser', password='1X<12345+tuK',
        )
        self.assertTrue(logged_in)
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Tests whether the correct template is used
        when user is logged in
        """
        test_user = User.objects.get(username='testuser')
        logged_in = self.client.login(
            username='testuser', password='1X<12345+tuK')
        self.assertTrue(logged_in)
        response = self.client.get(reverse('profile'))
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_user_can_edit_profile(self):
        """
        Tests whether logged in user can edit their profile
        """
        test_user = User.objects.get(username='testuser')
        logged_in = self.client.login(
            username='testuser', password='1X<12345+tuK')
        self.profile = UserProfile.objects.get(user=test_user)
        self.profile.default_full_name = 'Test Name'
        self.profile.save()
        response = self.client.post(
            reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.profile.default_full_name, 'Test Name')


class OrdersViewTest(TestCase):
    def setUp(self):
        """
        Sets up data for orders view tests
        """
        test_user = User.objects.create_user(
            username='testuser',
            email='testuser@email.com',
            password='1X<12345+tuK',
            is_staff=False,
        )
        test_user.save()

        self.profile = test_user.profile

    def test_unauthenticated_user_redirected(self):
        """
        Tests whether user is redirected if not logged in
        """
        test_user = User.objects.get(username='testuser')
        response = self.client.get(reverse(
            'orders'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_authenticated_user_can_access(self):
        """
        Tests whether authenticated user is granted access
        to their orders page
        """
        test_user = User.objects.get(username='testuser')
        logged_in = self.client.login(
            username='testuser', password='1X<12345+tuK',
        )
        self.assertTrue(logged_in)
        response = self.client.get('/profile/order_history/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Tests whether the correct template is used
        when user is logged in
        """
        test_user = User.objects.get(username='testuser')
        logged_in = self.client.login(
            username='testuser', password='1X<12345+tuK')
        self.assertTrue(logged_in)
        response = self.client.get(reverse('orders'))
        self.assertTemplateUsed(response, 'profiles/orders.html')


class OrderHistoryViewTest(TestCase):
    def setUp(self):
        """
        Sets up data for order history view tests
        """
        test_user = User.objects.create_user(
            username='testuser',
            email='testuser@email.com',
            password='1X<12345+tuK',
            is_staff=False,
        )
        test_user.save()

        self.profile = test_user.profile

        order1 = Order.objects.create(
            order_number = '1135862',
            user_profile = self.profile,
            grand_total = 57.55,
        )
        order2 = Order.objects.create(
            order_number = '4059872578',
            user_profile = self.profile,
            grand_total = 15.33,
        )

    def test_unauthenticated_user_can_acces_order(self):
        """
        Tests whether an unauthenticated user can access
        the page with their order details as long as they have
        their order number
        """
        test_user = User.objects.get(username='testuser')
        order = Order.objects.get(order_number='1135862')
        response = self.client.get(reverse(
            'order_history', args=[order.order_number]))
        self.assertEqual(response.status_code, 200)

    def test_authenticated_user_can_access(self):
        """
        Tests whether authenticated user is granted access
        to their order's page
        """
        test_user = User.objects.get(username='testuser')
        logged_in = self.client.login(
            username='testuser', password='1X<12345+tuK',
        )
        self.assertTrue(logged_in)
        order1 = Order.objects.get(order_number='1135862')
        response = self.client.get(f'/profile/order_history/{order1.order_number}/')
        self.assertEqual(response.status_code, 200)
        order2 = Order.objects.get(order_number='4059872578')
        response = self.client.get(f'/profile/order_history/{order2.order_number}/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Tests whether the correct template is used
        """
        test_user = User.objects.get(username='testuser')
        logged_in = self.client.login(
            username='testuser', password='1X<12345+tuK')
        order = Order.objects.get(order_number='1135862')
        response = self.client.get(reverse('order_history', args=[order.order_number]))
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')


class WishlistItemsViewTest(TestCase):
    def setUp(self):
        """
        Sets up data for wishlist items view tests
        """
        test_user = User.objects.create_user(
            username='testuser',
            email='testuser@email.com',
            password='1X<12345',
            is_staff=False,
        )
        test_user.save()

        self.profile = test_user.profile
    
    def test_unauthenticated_user_redirected(self):
        """
        Tests whether user is redirected if not logged in
        """
        test_user = User.objects.get(username='testuser')
        response = self.client.get(reverse(
            'wishlist_items'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_authenticated_user_can_access(self):
        """
        Tests whether authenticated user is granted access
        to their orders page
        """
        test_user = User.objects.get(username='testuser')
        logged_in = self.client.login(
            username='testuser', password='1X<12345',
        )
        response = self.client.get('/profile/wishlist_items/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Tests whether the correct template is used
        """
        test_user = User.objects.get(username='testuser')
        logged_in = self.client.login(
            username='testuser', password='1X<12345')
        response = self.client.get(reverse('wishlist_items'))
        self.assertTemplateUsed(response, 'profiles/wishlist.html')


class BookmarkedViewTest(TestCase):
    def setUp(self):
        """
        Sets up data for wishlist items view tests
        """
        test_user = User.objects.create_user(
            username='testuser',
            email='testuser@email.com',
            password='1X<12345',
            is_staff=False,
        )
        test_user.save()

        self.profile = test_user.profile
    
    def test_unauthenticated_user_redirected(self):
        """
        Tests whether user is redirected if not logged in
        """
        test_user = User.objects.get(username='testuser')
        response = self.client.get(reverse(
            'bookmarked'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_authenticated_user_can_access(self):
        """
        Tests whether authenticated user is granted access
        to their orders page
        """
        test_user = User.objects.get(username='testuser')
        logged_in = self.client.login(
            username='testuser', password='1X<12345',
        )
        response = self.client.get('/profile/bookmarked/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Tests whether the correct template is used
        """
        test_user = User.objects.get(username='testuser')
        logged_in = self.client.login(
            username='testuser', password='1X<12345')
        response = self.client.get(reverse('bookmarked'))
        self.assertTemplateUsed(response, 'profiles/bookmarked.html')
