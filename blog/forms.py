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
            'published',
            'date_of_publication',
            'related_products',
        ]
        widgets = {
            'content': SummernoteWidget(),
        }

