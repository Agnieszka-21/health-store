from django.test import SimpleTestCase, TestCase
from django_summernote.widgets import SummernoteWidget

from ..forms import ArticleForm, RestrictedArticleForm, RecipeForm, RestrictedRecipeForm


class ArticleFormTest(SimpleTestCase):

    def test_form_fields(self):
        """
        Tests which fields this form has
        """
        form = ArticleForm()
        self.assertTrue(form.Meta.fields, [
            'title',
            'banner_img',
            'img_title',
            'content',
            'keywords',
            'approved',
            'date_of_publication',
            'related_products',
        ])

    def test_keywords_help_text(self):
        """
        Tests help text for the field 'keywords'
        """
        form = ArticleForm()
        keywords_help = 'Separate keywords (words and/or phrases) \
            with a comma'
        self.assertTrue(form.fields['keywords'].help_text == keywords_help)

    def test_content_is_summernote(self):
        """
        Tests whether the field 'content' is a  Summernote
        widget
        """
        form = ArticleForm()
        self.assertTrue(
            form.fields['content'].widget, SummernoteWidget())

    def test_related_products_are_checkboxes(self):
        """
        Tests whether the field 'related_products' has multiple
        checkboxes
        """
        form = ArticleForm()
        self.assertEqual(
            form.fields['related_products'].widget.__class__.__name__,
            'CheckboxSelectMultiple')


class RestrictedArticleFormTest(SimpleTestCase):

    def test_user_field_is_excluded(self):
        """
        Tests whether the model field 'approved' is excluded
        """
        form = RestrictedArticleForm()
        self.assertEqual(form.Meta.exclude, ['approved', 'date_of_publication'])


class RecipeFormTest(SimpleTestCase):

    def test_form_fields(self):
        """
        Tests which fields this form has
        """
        form = RecipeForm()
        self.assertTrue(form.Meta.fields, [
            'title',
            'banner_img',
            'img_title',
            'description',
            'ingredients',
            'method',
            'keywords',
            'approved',
            'date_of_publication',
            'related_products',
        ])

    def test_keywords_help_text(self):
        """
        Tests help text for the field 'keywords'
        """
        form = RecipeForm()
        keywords_help = 'Separate keywords (words and/or phrases) \
            with a comma'
        self.assertTrue(form.fields['keywords'].help_text == keywords_help)

    def test_description_is_summernote(self):
        """
        Tests whether the field 'description' is a  Summernote
        widget
        """
        form = RecipeForm()
        self.assertTrue(
            form.fields['description'].widget, SummernoteWidget())

    def test_ingredients_is_summernote(self):
        """
        Tests whether the field 'ingredients' is a  Summernote
        widget
        """
        form = RecipeForm()
        self.assertTrue(
            form.fields['ingredients'].widget, SummernoteWidget())

    def test_method_is_summernote(self):
        """
        Tests whether the field 'method' is a  Summernote
        widget
        """
        form = RecipeForm()
        self.assertTrue(
            form.fields['method'].widget, SummernoteWidget())

    def test_related_products_are_checkboxes(self):
        """
        Tests whether the field 'related_products' has multiple
        checkboxes
        """
        form = RecipeForm()
        self.assertEqual(
            form.fields['related_products'].widget.__class__.__name__,
            'CheckboxSelectMultiple')


class RestrictedRecipeFormTest(SimpleTestCase):

    def test_user_field_is_excluded(self):
        """
        Tests whether the model field 'approved' is excluded
        """
        form = RestrictedRecipeForm()
        self.assertEqual(form.Meta.exclude, ['approved', 'date_of_publication'])
