from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Article, Recipe, Reading, FavouriteRecipe
from profiles.models import UserProfile


class ArticleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Sets up non-modified Article object
        used by all test methods
        """
        Article.objects.create(title='Test Article Title')

    def test_title_max_length(self):
        """
        Tests the maximum length of the field 'title'
        """
        article = Article.objects.get(id=1)
        max_length = article._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_slug_max_length(self):
        """
        Tests the maximum length of the field 'title'
        """
        article = Article.objects.get(id=1)
        max_length = article._meta.get_field('slug').max_length
        self.assertEqual(max_length, 200)

    def test_img_title_max_length(self):
        """
        Tests the maximum length of the field 'img_title'
        """
        article = Article.objects.get(id=1)
        max_length = article._meta.get_field('img_title').max_length
        self.assertEqual(max_length, 150)

    def test_keywords_max_length(self):
        """
        Tests the maximum length of the field 'keywords'
        """
        article = Article.objects.get(id=1)
        max_length = article._meta.get_field('keywords').max_length
        self.assertEqual(max_length, 300)

    def test_approved_is_false_by_default(self):
        """
        Tests whether the value of the field 'approved'
        is False by default
        """
        article = Article.objects.get(id=1)
        self.assertFalse(article.approved)

    def test_published_is_false_by_default(self):
        """
        Tests whether the value of the field 'published'
        is False by default
        """
        article = Article.objects.get(id=1)
        self.assertFalse(article.published)

    def test_articles_ordering(self):
        """
        Tests the ordering of Article objects
        """
        article = Article.objects.get(id=1)
        ordering = article._meta.ordering
        self.assertEqual(ordering, ['-date_of_publication'])

    def test_str_representation_is_title(self):
        """
        Tests string representation of the Article object
        """
        article = Article.objects.get(id=1)
        expected_str = f'{article.title}'
        self.assertEqual(str(article), expected_str)


class RecipeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Sets up non-modified Recipe object
        used by all test methods
        """
        Recipe.objects.create(title='Test Recipe Title')

    def test_title_max_length(self):
        """
        Tests the maximum length of the field 'title'
        """
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_slug_max_length(self):
        """
        Tests the maximum length of the field 'title'
        """
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('slug').max_length
        self.assertEqual(max_length, 200)

    def test_img_title_max_length(self):
        """
        Tests the maximum length of the field 'img_title'
        """
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('img_title').max_length
        self.assertEqual(max_length, 150)

    def test_keywords_max_length(self):
        """
        Tests the maximum length of the field 'keywords'
        """
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('keywords').max_length
        self.assertEqual(max_length, 300)

    def test_approved_is_false_by_default(self):
        """
        Tests whether the value of the field 'approved'
        is False by default
        """
        recipe = Recipe.objects.get(id=1)
        self.assertFalse(recipe.approved)

    def test_published_is_false_by_default(self):
        """
        Tests whether the value of the field 'published'
        is False by default
        """
        recipe = Recipe.objects.get(id=1)
        self.assertFalse(recipe.published)

    def test_recipes_ordering(self):
        """
        Tests the ordering of Article objects
        """
        recipe = Recipe.objects.get(id=1)
        ordering = recipe._meta.ordering
        self.assertEqual(ordering, ['-date_of_publication'])

    def test_str_representation_is_title(self):
        """
        Tests string representation of the Recipe object
        """
        recipe = Recipe.objects.get(id=1)
        expected_str = f'{recipe.title}'
        self.assertEqual(str(recipe), expected_str)


class ReadingModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Sets up non-modified Reading object
        used by all test methods
        """
        cls.user = User.objects.create_user(
            id=12345, username='Jack Sparrow'
        )
        cls.profile = cls.user.profile
        cls.reading = cls.profile

    def test_verbose_name_plural(self):
        """
        Tests the plural verbose name of the Reading object that was
        set explicitly since the default version lacked clarity
        """
        reading_list = Reading.objects.get(id=1)
        verbose_name_plural = reading_list._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, 'Favourite articles')

    def test_user_profile_has_reading_list(self):
        """
        Tests whether a user profile has its related
        reading list
        """
        profile = UserProfile.objects.get(id=1)
        reading_list = Reading.objects.get(id=1)
        self.assertEqual(self.profile.reading_list, reading_list)
        self.assertEqual(reading_list.user_profile, self.profile)


class FavouriteRecipeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Sets up non-modified FavouriteRecipe object
        used by all test methods
        """
        cls.user = User.objects.create_user(
            id=12345, username='Jack Sparrow'
        )
        cls.profile = cls.user.profile
        cls.favourite_recipes = cls.profile

    def test_user_profile_has_favourite_recipes(self):
        """
        Tests whether a user profile has its related
        list for favourite recipes
        """
        profile = UserProfile.objects.get(id=1)
        favourite_recipes = FavouriteRecipe.objects.get(id=1)
        self.assertEqual(self.profile.fav_recipe_list, favourite_recipes)
        self.assertEqual(favourite_recipes.user_profile, self.profile)
        self.assertTrue(self.profile.fav_recipe_list)
