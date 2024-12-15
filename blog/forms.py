from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from .models import Article, Recipe


class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = '__all__'

