from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Article, Recipe
from products.models import Product


RELATED_PRODUCT_CHOICES = Product.objects.all()


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'banner_img',
            'img_title',
            'content',
            'keywords',
            'approved',
            'date_of_publication',
            'related_products',
        ]
        help_texts = {
            'keywords': 'Separate keywords (words and/or phrases) \
            with a comma',
        }
        widgets = {
            'content': SummernoteWidget(),
            'date_of_publication': forms.TextInput(
                attrs={'placeholder': 'yyyy-mm-dd'}),
            'related_products': forms.CheckboxSelectMultiple(
                choices=RELATED_PRODUCT_CHOICES),
        }


class RestrictedArticleForm(ArticleForm):
    class Meta(ArticleForm.Meta):
        exclude = ['approved']


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
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
        ]
        help_texts = {
            'keywords': 'Separate keywords (words and/or phrases) \
            with a comma',
        }
        widgets = {
            'description': SummernoteWidget(),
            'ingredients': SummernoteWidget(),
            'method': SummernoteWidget(),
            'date_of_publication': forms.TextInput(
                attrs={'placeholder': 'yyyy-mm-dd'}),
            'related_products': forms.CheckboxSelectMultiple(
                choices=RELATED_PRODUCT_CHOICES),
        }


class RestrictedRecipeForm(RecipeForm):
    class Meta(RecipeForm.Meta):
        exclude = ['approved']
