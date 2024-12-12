from django.shortcuts import render
from django.views import generic

from .models import Article, Recipe


def choose_articles_or_recipes(request):
    return render(request, 'blog/blog_options.html')


class ArticlesList(generic.ListView):
    """
    Returns all articles in :model:`blog.Article`

    **Context**

    ``queryset``
        All  instances of :model:`blog.Article`

    **Template:**

    :template:`blog/articles.html`
    """
    queryset = Article.objects.all()
    template_name = 'blog/articles.html'


class RecipesList(generic.ListView):
    """
    Returns all articles in :model:`blog.Recipe`

    **Context**

    ``queryset``
        All  instances of :model:`blog.Recipe`

    **Template:**

    :template:`blog/recipes.html`
    """
    queryset = Recipe.objects.all()
    template_name = 'blog/recipes.html'

