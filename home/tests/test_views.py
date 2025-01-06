from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse

from ..models import Carousel


class HomeViewTest(TestCase):

    def test_view_uses_correct_template(self):
        """
        Tests whether the correct template is used
        """
        response = self.client.get('')
        self.assertTemplateUsed('home/index.html')


class AdminAccessViewsTest(TestCase):

    def setUp(self):
        """
        Creates a superuser to run tests for views accessible
        only to admins
        """
        username = 'AdminUser'
        email = 'tester@test.com'
        password = 'testPassword12345'
        user_model = get_user_model()
        self.user = user_model.objects.create_superuser(
            username=username,
            email=email,
            password=password,
        )
        log_in = self.client.login(email=email, password=password)

        # Confirm user is logged in
        self.assertTrue(log_in)
        self.assertTrue(self.user.is_superuser)
        # Create a carousel for the test database
        self.carousel1 = Carousel.objects.create(
            title='Test carousel',
            display=True,
        )
        self.carousel2 = Carousel.objects.create(
            title='Default carousel',
            display=False,
        )
        carousels = Carousel.objects.all()

    def test_admin_panel_page(self):
        """
        Tests the admin panel page url
        """
        response = self.client.get('/admin_panel/')
        self.assertEqual(response.status_code, 200)

    def test_admin_panel_uses_correct_template(self):
        """
        Tests whether the correct template is used
        """
        response = self.client.get(reverse('admin_panel'))
        self.assertTemplateUsed(response,
                                template_name='home/admin_panel.html')

    def test_create_carousel_page(self):
        """
        Tests the create carousel page url
        """
        response = self.client.get('/create_carousel/')
        self.assertEqual(response.status_code, 200)

    def test_create_carousel_uses_correct_template(self):
        """
        Tests whether the correct template is used
        """
        response = self.client.get(reverse('create_carousel'))
        self.assertTemplateUsed(response,
                                template_name='home/create_carousel.html')

    def test_choose_carousel_page(self):
        """
        Tests the choose carousel page url
        """
        response = self.client.get('/choose_carousel/')
        self.assertEqual(response.status_code, 200)

    def test_choose_carousel_uses_correct_template(self):
        """
        Tests whether the correct template is used
        """
        response = self.client.get(reverse('choose_carousel'))
        self.assertTemplateUsed(response,
                                template_name='home/choose_carousel.html')

    def test_edit_carousel_page(self):
        """
        Tests the edit carousel page url
        """
        response = self.client.get(reverse('edit_carousel',
                                           args=[self.carousel1.id]))
        self.assertEqual(response.status_code, 200)

    def test_edit_carousel_uses_correct_template(self):
        """
        Tests whether the correct template is used
        """
        response = self.client.get(reverse('edit_carousel',
                                           args=[self.carousel1.id]))
        self.assertTemplateUsed(response,
                                template_name='home/edit_carousel.html')

    def test_delete_carousel_page(self):
        """
        Tests the delete carousel page url
        """
        response = self.client.get(reverse('delete_carousel',
                                           args=[self.carousel1.id]))
        self.assertEqual(response.status_code, 200)

    def test_delete_carousel_uses_correct_template(self):
        """
        Tests whether the correct template is used
        """
        response = self.client.get(reverse('delete_carousel',
                                           args=[self.carousel1.id]))
        self.assertTemplateUsed(response,
                                template_name='home/delete_carousel.html')

    def test_deleting_carousel(self):
        """
        Tests delete carousel view
        """
        carousel = Carousel.objects.get(title='Test carousel')
        self.assertEqual(Carousel.objects.count(), 2)
        response = self.client.post(reverse(
            'delete_carousel', args=[carousel.id]))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].tags, 'success')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Carousel.objects.count(), 1)

    def test_logged_out_user_admin_panel(self):
        """"
        Tests if a logged out user is redirected
        so that they cannot access the admin panel page
        """
        self.client.logout()
        response = self.client.get(reverse(
            'admin_panel'))
        self.assertEqual(response.status_code, 302)

    def test_logged_out_user_create_carousel(self):
        """"
        Tests if a logged out user is redirected
        so that they cannot create a carousel
        """
        self.client.logout()
        response = self.client.get(reverse(
            'create_carousel'))
        self.assertEqual(response.status_code, 302)
