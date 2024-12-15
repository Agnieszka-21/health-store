from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic.list import ListView
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Article, Recipe
from .forms import ArticleForm


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
    queryset = Article.objects.all()
    template_name = 'blog/articles.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        published_articles = Article.objects.filter(published=True)
        context['now'] = timezone.now()
        context['published_articles'] = published_articles

        unpublished_articles = Article.objects.filter(published=False)
        context['unpublished_articles'] = unpublished_articles

        print('All articles: ', self.object_list)
        print('All published articles: ', published_articles)
        print('All unpublished articles: ', unpublished_articles)
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


def article_detail(request, article_id):
    """
    Display an individual :model:`blog.Article`.

    **Context**

    ``article``
        An instance of :model:`blog.Article`.

    **Template:**

    :template:`blog/article_detail.html`
    """

    # queryset = Article.objects.filter(published=True)
    queryset = Article.objects.all()
    article = get_object_or_404(queryset, pk=article_id)
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


@login_required
def edit_article(request, article_id):
    """ Edit a product in the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store managers can edit a blog article.')
        return redirect(reverse('home'))

    article = get_object_or_404(Article, pk=article_id)

    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES, instance=article)

        if article_form.is_valid():
            edited_article = article_form.save()
            messages.success(request, 'Successfully updated the article')
            return redirect(reverse('article_detail', args=[edited_article.id]))
        else:
            messages.error(request, 'Failed to update article. Please ensure the form is valid.')
    else:
        article_form = ArticleForm(instance=article)
        messages.info(request, f'You are editing {article.title}')

    template = 'blog/edit_article.html'
    context = {
        'article_form': article_form,
        'article': article,
    }

    return render(request, template, context)


@login_required
def unpublish_article(request, article_id):
    """ Delete a product from the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store managers can unpublish a blog article.')
        return redirect(reverse('home'))

    article = get_object_or_404(Article, pk=article_id)
    article.published = False
    article.save()
    messages.success(request, 'Article unpublished successfully')
    return redirect(reverse('articles'))
