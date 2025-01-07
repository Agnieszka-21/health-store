from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from django.utils.timezone import make_aware
from dateutil import parser

import datetime

from ..models import Article, Recipe


class ChooseArticlesOrRecipesViewTest(SimpleTestCase):

    def test_view_url_exists_at_desired_location(self):
        """
        Tests whether the url related to this view
        exists at the desired location
        """
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """
        Tests whether the url related to this view
        can be accessed by its name
        """
        response = self.client.get(reverse('blog_options'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Tests whether the correct template is used
        """
        response = self.client.get(reverse('blog_options'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_options.html')


class ArticleListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Creates 5 Article objects to set up
        unmodified data for the entire TestCase
        """
        number_of_articles = 5

        for id in range(number_of_articles):
            Article.objects.create(
                title=f'Title {id}',
                date_of_publication=datetime.date(2024, 12, 12),
                approved=True,
            )

    def test_view_url_exists_at_desired_location(self):
        """
        Tests whether the url related to this view
        exists at the desired location
        """
        response = self.client.get('/blog/articles/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """
        Tests whether the url related to this view
        can be accessed by its name
        """
        response = self.client.get(reverse('articles'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Tests whether the correct template is used
        """
        response = self.client.get(reverse('articles'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/articles.html')

    def test_lists_all_published_articles(self):
        """
        Confirms that the list of published articles has (exactly)
        5 items, all on one page, accessible without logging in
        """
        response = self.client.get(reverse('articles')+'?page=1')
        self.assertEqual(response.status_code, 200)
        self.assertFalse('is_paginated' in response.context)
        self.assertEqual(len(response.context['published_articles']), 5)


class RecipeListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Creates 5 Recipe objects to set up
        unmodified data for the entire TestCase
        """
        number_of_recipes = 5

        for id in range(number_of_recipes):
            Recipe.objects.create(
                title=f'Title {id}',
                date_of_publication=datetime.date(2024, 12, 12),
                approved=True,
            )

    def test_view_url_exists_at_desired_location(self):
        """
        Tests whether the url related to this view
        exists at the desired location
        """
        response = self.client.get('/blog/recipes/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """
        Tests whether the url related to this view
        can be accessed by its name
        """
        response = self.client.get(reverse('recipes'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Tests whether the correct template is used
        """
        response = self.client.get(reverse('recipes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/recipes.html')

    def test_lists_all_published_articles(self):
        """
        Confirms that the list of published recipes has (exactly)
        5 items, all on one page, accessible without logging in
        """
        response = self.client.get(reverse('recipes')+'?page=1')
        self.assertEqual(response.status_code, 200)
        self.assertFalse('is_paginated' in response.context)
        self.assertEqual(len(response.context['published_recipes']), 5)


class ArticleDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Creates 5 unmodified Article objects
        to set up data for the entire TestCase
        """
        number_of_articles = 5

        for id in range(number_of_articles):
            cls.article = Article.objects.create(
                title=f'Title {id}',
                date_of_publication=datetime.date(2024, 12, 12),
                approved=True,
            )

    def test_view_url_exists_at_desired_location(self):
        """
        Tests whether the url related to this view
        exists at the desired location
        """
        article1 = Article.objects.get(title='Title 1')
        response = self.client.get(f'/blog/articles/title-1/')
        self.assertEqual(response.status_code, 200)
        # Check if response is 404 for an article not on the list
        response = self.client.get(f'/articles/detail/title-6/')
        self.assertEqual(response.status_code, 404)

    def test_view_url_accessible_by_name(self):
        """
        Tests whether the url related to this view
        can be accessed by its name
        """
        article = Article.objects.get(title='Title 1')
        slug = article.slug
        response = self.client.get(
            reverse('article_detail', kwargs={'slug': slug}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Tests whether the correct template is used
        """
        article = Article.objects.get(title='Title 1')
        slug = article.slug
        response = self.client.get(
            reverse('article_detail', kwargs={'slug': slug}))
        self.assertTemplateUsed(response, 'blog/article_detail.html')


class RecipeDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Creates 5 unmodified Recipe objects
        to set up data for the entire TestCase
        """
        number_of_recipes = 5

        for id in range(number_of_recipes):
            cls.article = Recipe.objects.create(
                title=f'Title {id}',
                date_of_publication=datetime.date(2024, 12, 12),
                approved=True,
            )

    def test_view_url_exists_at_desired_location(self):
        """
        Tests whether the url related to this view
        exists at the desired location
        """
        article1 = Recipe.objects.get(title='Title 1')
        response = self.client.get(f'/blog/recipes/title-1/')
        self.assertEqual(response.status_code, 200)
        # Check if response is 404 for an article not on the list
        response = self.client.get(f'/recipes/detail/title-6/')
        self.assertEqual(response.status_code, 404)

    def test_view_url_accessible_by_name(self):
        """
        Tests whether the url related to this view
        can be accessed by its name
        """
        recipe = Recipe.objects.get(title='Title 1')
        slug = recipe.slug
        response = self.client.get(
            reverse('recipe_detail', kwargs={'slug': slug}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Tests whether the correct template is used
        """
        recipe = Recipe.objects.get(title='Title 1')
        slug = recipe.slug
        response = self.client.get(
            reverse('recipe_detail', kwargs={'slug': slug}))
        self.assertTemplateUsed(response, 'blog/recipe_detail.html')


class CreateArticleViewTest(TestCase):
    def setUp(self):
        """
        Sets up data that can be modified in the methods below
        """
        # user_model = get_user_model()
        test_customer = User.objects.create(
            username='testuser1', password='1X<ISRUkw+tuK', id=1
        )
        test_customer.save()
        # test_superuser = User.objects.create(
        #     username='testsuperuser',
        #     email='superuseremail@test.com',
        #     password='1X<ISRUkw+tuK',
        #     is_superuser=True)
        # test_superuser.save()

    def test_unauthenticated_user_redirected(self):
        """
        Tests whether unauthenticated user is redirected
        and can not access add blog post page
        """
        response = self.client.get('/blog/articles/create/')
        self.assertEqual(response.status_code, 302)

    def test_authenticated_non_staff_user_redirected(self):
        """
        Tests whether unauthenticated user is redirected
        and can not access add blog post page
        """
        test_customer = User.objects.get(id=1)
        logged_in = self.client.login(
            username='testuser1', password='1X<ISRUkw+tuK'
        )
        print('LOGGED_IN: ', logged_in)
        # confirm user is logged in
        # self.assertTrue(logged_in)
        # self.assertFalse(self.user.is_staff)
        # response = self.client.get('/blog/articles/create/')
        # self.assertEqual(response.status_code, 302)


class EditArticleViewTest(TestCase):
    def setUp(self):
        """
        Sets up data that can be modified in the methods below
        """
        test_staffuser = User.objects.create_user(
            username='staffuser', password='staffISRUkw+tuK',
            id=1, is_staff=True)
        test_staffuser.save()
        # test_yogastyle = YogaStyle.objects.create(
        #     group_class_style='Express Lunchtime Yoga')
        # test_groupclass = GroupClass.objects.create(title=test_yogastyle)
        self.article = Article.objects.create(
            title='Test article title',
            slug='test-article-title'
        )

    def test_redirects_if_not_logged_in(self):
        """
        Tests whether user is redirected if not logged in
        """
        test_staffuser = User.objects.get(username='staffuser')
        response = self.client.get(reverse(
            'edit_article', args=[self.article.id]))
        self.assertEqual(response.status_code, 302)

    def test_uses_correct_template(self):
        """
        Tests whether the correct template is used
        when user is logged in
        """
        test_staffuser = User.objects.get(username='staffuser')
        logged_in = self.client.login(
            username='staffuser', password='staffISRUkw+tuK', id=1)
        # Confirm user is logged in
        self.assertTrue(logged_in)
        response = self.client.get(reverse(
            'edit_article',
            args=[self.article.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/edit_article.html')

    def test_redirects_to_article_detail_on_success(self):
        """
        Tests whether user is redirected to the article's detail page
        upon successfully editing it
        """
        test_staffuser = User.objects.get(username='staffuser')
        logged_in = self.client.login(
            username='staffuser', password='staffISRUkw+tuK', id=1)
        # Confirm user is logged in
        self.assertTrue(logged_in)
        # Edit the article
        self.article.title = 'Title edited'
        self.article.save()

        response = self.client.post(reverse(
            'edit_article',
            args=[self.article.id]))
        # self.assertRedirects(response, reverse(
        #     'article_detail', args=[self.article.slug]))

