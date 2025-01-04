from django.test import TestCase

from ..models import Carousel


class HomeViewTest(TestCase):

    def test_view_uses_correct_template(self):
        """
        Tests whether the correct template is used
        """
        response = self.client.get('')
        self.assertTemplateUsed('home/index.html')


class Error404ViewTest(TestCase):

    def test_view_uses_correct_template(self):
        """
        Tests whether the correct template is used
        """
        response = self.client.get('/404/')
        self.assertTemplateUsed('home/error404.html')


class Error500ViewTest(TestCase):

    def test_view_uses_correct_template(self):
        """
        Tests whether the correct template is used
        """
        response = self.client.get('/500/')
        self.assertTemplateUsed('home/error500.html')




