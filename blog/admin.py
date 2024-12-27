from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Article, Recipe, Reading, FavouriteRecipe


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'published')
    search_fields = ['title']
    list_filter = ('published',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'published')
    search_fields = ['title']
    list_filter = ('published',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description', 'ingredients', 'method')


admin.site.register(Reading)
admin.site.register(FavouriteRecipe)
