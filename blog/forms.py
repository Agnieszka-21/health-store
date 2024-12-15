from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Article, Recipe


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
        widgets = {
            'content': SummernoteWidget(),
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
        widgets = {
            'description': SummernoteWidget(),
            'ingredients': SummernoteWidget(),
            'method': SummernoteWidget(),
        }


class RestrictedRecipeForm(RecipeForm):
    class Meta(RecipeForm.Meta):
        exclude = ['approved']
