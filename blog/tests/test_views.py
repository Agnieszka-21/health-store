from django.contrib.auth.models import User
from django.test import SimpleTestCase, TestCase
from django.urls import reverse

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
        response = self.client.get(reverse('articles'))
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
        response = self.client.get(reverse('recipes'))
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


class ArticleAdminViewsTest(TestCase):
    def setUp(self):
        """
        Sets up data that can be modified in the methods below
        Used for the following **views:**

        :view:`create_article`
        :view:`edit_article`
        :view:`unpublish_article`
        :view:`delete_article`
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
        self.article = Article.objects.create(
            title='Test article title',
            img_title='Test image',
            content='Test content',
            keywords='test, keywords',
        )

    def test_create_unauthenticated_user_redirected(self):
        """
        Tests whether unauthenticated user is redirected
        and cannot access the add blog post page
        """
        response = self.client.get('/blog/articles/create/')
        self.assertEqual(response.status_code, 302)

    def test_create_authenticated_non_staff_user_redirected(self):
        """
        Tests whether unauthenticated user is redirected
        and cannot access the add blog post page
        """
        test_customer = User.objects.get(username='testuser')
        logged_in = self.client.login(
            username='testuser', password='1X<ISRUkw+tuK',
        )
        self.assertTrue(logged_in)
        self.assertFalse(test_customer.is_staff)
        response = self.client.get('/blog/articles/create/')
        self.assertEqual(response.status_code, 302)

    def test_create_staff_user_can_access(self):
        """
        Tests whether authenticated staff user is granted access
        to the article creation page
        """
        test_staffuser = User.objects.get(username='teststaffuser')
        logged_in = self.client.login(
            username='teststaffuser', password='staFF-useR',
        )
        self.assertTrue(logged_in)
        self.assertTrue(test_staffuser.is_staff)
        response = self.client.get('/blog/articles/create/')
        self.assertEqual(response.status_code, 200)

    def test_create_url_accessible_by_name(self):
        """
        Tests whether the url related to this view
        can be accessed by its name
        """
        test_staffuser = User.objects.get(username='teststaffuser')
        logged_in = self.client.login(
            username='teststaffuser', password='staFF-useR')
        response = self.client.get(
            reverse('create_article'))
        self.assertEqual(response.status_code, 200)

    def test_create_uses_correct_template(self):
        """
        Tests whether the correct template is used
        when user is logged in
        """
        test_staffuser = User.objects.get(username='teststaffuser')
        logged_in = self.client.login(
            username='teststaffuser', password='staFF-useR', id=1)
        response = self.client.get(reverse('create_article'))
        self.assertTemplateUsed(response, 'blog/create_article.html')

    def test_edit_redirects_if_not_logged_in(self):
        """
        Tests whether user is redirected if not logged in
        """
        test_staffuser = User.objects.get(username='teststaffuser')
        response = self.client.get(reverse(
            'edit_article', args=[self.article.id]))
        self.assertEqual(response.status_code, 302)

    def test_edit_url_accessible_by_name(self):
        """
        Tests whether the url related to this view
        can be accessed by its name
        """
        test_staffuser = User.objects.get(username='teststaffuser')
        logged_in = self.client.login(
            username='teststaffuser', password='staFF-useR')
        response = self.client.get(
            reverse('edit_article', args=[self.article.id]))
        self.assertEqual(response.status_code, 200)

    def test_edit_uses_correct_template(self):
        """
        Tests whether the correct template is used
        when staffuser is logged in
        """
        test_staffuser = User.objects.get(username='teststaffuser')
        logged_in = self.client.login(
            username='teststaffuser', password='staFF-useR')
        response = self.client.get(reverse(
            'edit_article',
            args=[self.article.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/edit_article.html')

    def test_unpublish_unauthenticated_user_redirected(self):
        """
        Tests whether user is redirected if not logged in
        """
        test_superuser = User.objects.get(username='testsuperuser')
        response = self.client.get(reverse(
            'unpublish_article', args=[self.article.id]))
        self.assertEqual(response.status_code, 302)

    def test_unpublish_staffuser_redirected(self):
        """
        Tests whether an authenticated staffuser is redirected
        """
        test_staffuser = User.objects.get(username='teststaffuser')
        response = self.client.get(reverse(
            'unpublish_article', args=[self.article.id]))
        self.assertEqual(response.status_code, 302)

    def test_unpublish_uses_correct_template(self):
        """
        Tests whether the correct template is used
        when superuser is logged in
        """
        test_superuser = User.objects.get(username='testsuperuser')
        logged_in = self.client.login(
            username='testsuperuser', password='suPeR42315')
        response = self.client.get(reverse(
            'unpublish_article',
            args=[self.article.id]))
        self.assertTemplateUsed(response, 'blog/delete_article.html')

    def test_unpublish_url_accessible_by_name(self):
        """
        Tests whether the url related to this view
        can be accessed by its name
        """
        test_superuser = User.objects.get(username='testsuperuser')
        logged_in = self.client.login(
            username='testsuperuser', password='suPeR42315')
        response = self.client.get(
            reverse('unpublish_article', args=[self.article.id]))
        self.assertEqual(response.status_code, 200)

    def test_superuser_can_unpublish_article(self):
        """
        Tests whether superuser can unpublish an article and
        whether they are redirected correctly upon success
        """
        test_superuser = User.objects.get(username='testsuperuser')
        logged_in = self.client.login(
            username='testsuperuser', password='suPeR42315')
        self.article.approved = False
        self.article.published = False
        self.article.save()
        response = self.client.post(
            reverse('unpublish_article', args=[self.article.id]))
        self.assertRedirects(response, reverse('articles'))
        # Ensure the article does not show up under published articles
        response = self.client.get(reverse('articles'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['published_articles']), 0)
        self.assertEqual(len(response.context['unpublished_articles']), 1)

    def test_delete_unauthenticated_user_redirected(self):
        """
        Tests whether user is redirected if not logged in
        """
        test_superuser = User.objects.get(username='testsuperuser')
        response = self.client.get(reverse(
            'delete_article', args=[self.article.id]))
        self.assertEqual(response.status_code, 302)

    def test_delete_staffuser_redirected(self):
        """
        Tests whether an authenticated staffuser is redirected
        """
        test_staffuser = User.objects.get(username='teststaffuser')
        response = self.client.get(reverse(
            'delete_article', args=[self.article.id]))
        self.assertEqual(response.status_code, 302)

    def test_delete_uses_correct_template(self):
        """
        Tests whether the correct template is used
        when superuser is logged in
        """
        test_superuser = User.objects.get(username='testsuperuser')
        logged_in = self.client.login(
            username='testsuperuser', password='suPeR42315')
        response = self.client.get(reverse(
            'delete_article',
            args=[self.article.id]))
        self.assertTemplateUsed(response, 'blog/delete_article.html')

    def test_delete_url_accessible_by_name(self):
        """
        Tests whether the url related to this view
        can be accessed by its name
        """
        test_superuser = User.objects.get(username='testsuperuser')
        logged_in = self.client.login(
            username='testsuperuser', password='suPeR42315')
        response = self.client.get(
            reverse('delete_article', args=[self.article.id]))
        self.assertEqual(response.status_code, 200)

    def test_superuser_can_delete_article(self):
        """
        Tests whether superuser can delete an article and
        whether they are redirected correctly upon success
        """
        test_superuser = User.objects.get(username='testsuperuser')
        logged_in = self.client.login(
            username='testsuperuser', password='suPeR42315')
        response = self.client.post(
            reverse('delete_article', args=[self.article.id]))
        self.article.delete()
        self.assertRedirects(response, reverse('articles'))


class RecipeAdminViewsTest(TestCase):
    def setUp(self):
        """
        Sets up data that can be modified in the methods below
        Used for the following **views:**

        :view:`create_recipe`
        :view:`edit_recipe`
        :view:`unpublish_recipe`
        :view:`delete_recipe`
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
        self.recipe = Recipe.objects.create(
            title='Test recipe title',
            img_title='Test image',
            description='Test description',
            ingredients='Test ingredients',
            method='Test method',
            keywords='test, keywords',
            date_of_publication=datetime.date(2024, 11, 11),
            approved=True,
        )

    def test_create_unauthenticated_user_redirected(self):
        """
        Tests whether user is redirected if not logged in
        """
        test_staffuser = User.objects.get(username='teststaffuser')
        response = self.client.get(reverse(
            'create_recipe'))
        self.assertEqual(response.status_code, 302)

    def test_create_authenticated_non_staff_user_redirected(self):
        """
        Tests whether unauthenticated user is redirected
        and can not access the add recipe page
        """
        test_customer = User.objects.get(username='testuser')
        logged_in = self.client.login(
            username='testuser', password='1X<ISRUkw+tuK',
        )
        self.assertTrue(logged_in)
        self.assertFalse(test_customer.is_staff)
        response = self.client.get('/blog/recipes/create/')
        self.assertEqual(response.status_code, 302)

    def test_create_staff_user_can_access(self):
        """
        Tests whether authenticated staffuser is granted access
        to the recipe creation page
        """
        test_staffuser = User.objects.get(username='teststaffuser')
        logged_in = self.client.login(
            username='teststaffuser', password='staFF-useR',
        )
        self.assertTrue(logged_in)
        self.assertTrue(test_staffuser.is_staff)
        response = self.client.get('/blog/recipes/create/')
        self.assertEqual(response.status_code, 200)

    def test_create_uses_correct_template(self):
        """
        Tests whether the correct template is used
        when staffuser is logged in
        """
        test_staffuser = User.objects.get(username='teststaffuser')
        logged_in = self.client.login(
            username='teststaffuser', password='staFF-useR')
        self.assertTrue(logged_in)
        response = self.client.get(reverse('create_recipe'))
        self.assertTemplateUsed(response, 'blog/create_recipe.html')

    def test_edit_redirects_if_not_logged_in(self):
        """
        Tests whether user is redirected if not logged in
        """
        test_staffuser = User.objects.get(username='teststaffuser')
        response = self.client.get(reverse(
            'edit_recipe', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 302)

    def test_edit_url_accessible_by_name(self):
        """
        Tests whether the url related to this view
        can be accessed by its name
        """
        test_staffuser = User.objects.get(username='teststaffuser')
        logged_in = self.client.login(
            username='teststaffuser', password='staFF-useR')
        response = self.client.get(
            reverse('edit_recipe', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 200)

    def test_edit_uses_correct_template(self):
        """
        Tests whether the correct template is used
        when staffuser is logged in
        """
        test_staffuser = User.objects.get(username='teststaffuser')
        logged_in = self.client.login(
            username='teststaffuser', password='staFF-useR')
        self.assertTrue(logged_in)
        response = self.client.get(reverse(
            'edit_recipe',
            args=[self.recipe.id]))
        self.assertTemplateUsed(response, 'blog/edit_recipe.html')

    def test_unpublish_unauthenticated_user_redirected(self):
        """
        Tests whether user is redirected if not logged in
        """
        test_superuser = User.objects.get(username='testsuperuser')
        response = self.client.get(reverse(
            'unpublish_recipe', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 302)

    def test_unpublish_staffuser_redirected(self):
        """
        Tests whether an authenticated staffuser is redirected
        """
        test_staffuser = User.objects.get(username='teststaffuser')
        response = self.client.get(reverse(
            'unpublish_recipe', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 302)

    def test_unpublish_uses_correct_template(self):
        """
        Tests whether the correct template is used
        when superuser is logged in
        """
        test_superuser = User.objects.get(username='testsuperuser')
        logged_in = self.client.login(
            username='testsuperuser', password='suPeR42315')
        response = self.client.get(reverse(
            'unpublish_recipe',
            args=[self.recipe.id]))
        self.assertTemplateUsed(response, 'blog/delete_recipe.html')

    def test_unpublish_url_accessible_by_name(self):
        """
        Tests whether the url related to this view
        can be accessed by its name
        """
        test_superuser = User.objects.get(username='testsuperuser')
        logged_in = self.client.login(
            username='testsuperuser', password='suPeR42315')
        response = self.client.get(
            reverse('unpublish_recipe', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 200)

    def test_superuser_can_unpublish_recipe(self):
        """
        Tests whether superuser can unpublish a recipe and
        whether they are redirected correctly upon success
        """
        test_superuser = User.objects.get(username='testsuperuser')
        logged_in = self.client.login(
            username='testsuperuser', password='suPeR42315')
        self.recipe.approved = False
        self.recipe.published = False
        self.recipe.save()
        response = self.client.post(
            reverse('unpublish_recipe', args=[self.recipe.id]))
        self.assertRedirects(response, reverse('recipes'))
        # Ensure the recipe does not show up under published recipes
        response = self.client.get(reverse('recipes'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['published_recipes']), 0)
        self.assertEqual(len(response.context['unpublished_recipes']), 1)

    def test_delete_unauthenticated_user_redirected(self):
        """
        Tests whether user is redirected if not logged in
        """
        test_superuser = User.objects.get(username='testsuperuser')
        response = self.client.get(reverse(
            'delete_recipe', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 302)

    def test_delete_staffuser_redirected(self):
        """
        Tests whether an authenticated staffuser is redirected
        """
        test_staffuser = User.objects.get(username='teststaffuser')
        response = self.client.get(reverse(
            'delete_recipe', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 302)

    def test_delete_uses_correct_template(self):
        """
        Tests whether the correct template is used
        when superuser is logged in
        """
        test_superuser = User.objects.get(username='testsuperuser')
        logged_in = self.client.login(
            username='testsuperuser', password='suPeR42315')
        response = self.client.get(reverse(
            'delete_recipe',
            args=[self.recipe.id]))
        self.assertTemplateUsed(response, 'blog/delete_recipe.html')

    def test_delete_url_accessible_by_name(self):
        """
        Tests whether the url related to this view
        can be accessed by its name
        """
        test_superuser = User.objects.get(username='testsuperuser')
        logged_in = self.client.login(
            username='testsuperuser', password='suPeR42315')
        response = self.client.get(
            reverse('delete_recipe', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 200)

    def test_superuser_can_delete_recipe(self):
        """
        Tests whether superuser can delete a recipe and
        whether they are redirected correctly upon success
        """
        test_superuser = User.objects.get(username='testsuperuser')
        logged_in = self.client.login(
            username='testsuperuser', password='suPeR42315')
        response = self.client.post(
            reverse('delete_recipe', args=[self.recipe.id]))
        self.recipe.delete()
        self.assertRedirects(response, reverse('recipes'))
