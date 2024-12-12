from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.utils import timezone

from .models import Article, Recipe


def choose_articles_or_recipes(request):
    return render(request, 'blog/blog_options.html')


class ArticleListView(ListView):
    """
    Returns all articles in :model:`blog.Article`

    **Context**

    ``queryset``
        All  instances of :model:`blog.Article`

    **Template:**

    :template:`blog/articles.html`
    """
    queryset = Article.objects.filter(published=True)
    template_name = 'blog/articles.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        print('All articles: ', self.object_list)
        return context


class RecipeListView(ListView):
    """
    Returns all articles in :model:`blog.Recipe`

    **Context**

    ``queryset``
        All  instances of :model:`blog.Recipe`

    **Template:**

    :template:`blog/recipes.html`
    """
    queryset = Recipe.objects.filter(published=True)
    template_name = 'blog/recipes.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        print('All recipes: ', self.object_list)
        return context


def article_detail(request, slug):
    """
    Display an individual :model:`blog.Article`.

    **Context**

    ``article``
        An instance of :model:`blog.Article`.

    **Template:**

    :template:`blog/article_detail.html`
    """

    queryset = Article.objects.filter(published=True)
    article = get_object_or_404(queryset, slug=slug)
    template = 'blog/article_detail.html'
    context = {'article': article}

    return render(request, template, context)


def recipe_detail(request, slug):
    """
    Display an individual :model:`blog.Recipe`.

    **Context**

    ``article``
        An instance of :model:`blog.Recipe`.

    **Template:**

    :template:`blog/recipe_detail.html`
    """

    queryset = Recipe.objects.filter(published=True)
    recipe = get_object_or_404(queryset, slug=slug)
    template = 'blog/recipe_detail.html'
    context = {'recipe': recipe}

    return render(request, template, context)
