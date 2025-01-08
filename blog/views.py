from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.utils import timezone
from django.views.generic.list import ListView

import datetime

from .forms import (
    ArticleForm, RestrictedArticleForm, RecipeForm, RestrictedRecipeForm)
from .models import Article, Recipe, Reading, FavouriteRecipe


def choose_articles_or_recipes(request):
    """
    Renders the tempalte where user chooses articles/recipes

    **Template:**

    :template: `blog/blog_options.html`
    """
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

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        published_articles = Article.objects.filter(published=True)
        scheduled_for_publication = Article.objects.filter(
            approved=True, published=False)

        scheduled_list = list(scheduled_for_publication)

        for article in scheduled_for_publication:
            if article.date_of_publication is None:
                scheduled_list.remove(article)

        scheduled_for_publication = scheduled_list

        unpublished_articles = Article.objects.filter(
            approved=False, published=False)
        context = {
            'published_articles': published_articles,
            'unpublished_articles': unpublished_articles,
            'scheduled_for_publication': scheduled_for_publication
        }

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
    queryset = Recipe.objects.all()
    template_name = 'blog/recipes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        published_recipes = Recipe.objects.filter(published=True)
        scheduled_for_publication = Recipe.objects.filter(
            approved=True, published=False)
        unpublished_recipes = Recipe.objects.filter(
            approved=False, published=False)
        context = {
            'published_recipes': published_recipes,
            'unpublished_recipes': unpublished_recipes,
            'scheduled_for_publication': scheduled_for_publication
        }

        return context


def article_detail(request, slug):
    """
    Displays an individual :model:`blog.Article`.

    **Context**

    ``article``
    An instance of :model:`blog.Article`.

    **Template:**

    :template:`blog/article_detail.html`
    """
    queryset = Article.objects.all()
    article = get_object_or_404(queryset, slug=slug)
    template = 'blog/article_detail.html'
    context = {'article': article}

    return render(request, template, context)


def recipe_detail(request, slug):
    """
    Displays an individual :model:`blog.Recipe`.

    **Context**

    ``article``
    An instance of :model:`blog.Recipe`.

    **Template:**

    :template:`blog/recipe_detail.html`
    """
    queryset = Recipe.objects.all()
    recipe = get_object_or_404(queryset, slug=slug)
    template = 'blog/recipe_detail.html'
    context = {'recipe': recipe}

    return render(request, template, context)


@login_required
def create_article(request):
    """
    Adds a new article on the blog - for staff only

    **Context**

    ``article_form``
    :form:`RestrictedArticleForm`

    **Template:**

    :template:`blog/create_article.html`
    """
    if not request.user.is_staff:
        messages.error(
            request, 'Sorry, only store employees can add a blog article.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        article_form = RestrictedArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            added_article = article_form.save()
            messages.success(
                request, 'Successfully created and saved article!')
            return redirect(
                reverse('article_detail', args=[added_article.slug]))
        else:
            messages.error(
                request, 'Failed to add article. \
                Please ensure the form is valid.')
    else:
        article_form = RestrictedArticleForm()

    template = 'blog/create_article.html'
    context = {'article_form': article_form}

    return render(request, template, context)


@login_required
def create_recipe(request):
    """
    Adds a new recipe on the blog - for staff only

    **Context**

    ``recipe_form``
    :form:`RestrictedRecipeForm`

    **Template:**

    :template:`blog/create_recipe.html`
    """
    if not request.user.is_staff:
        messages.error(
            request, 'Sorry, only store employees can add a recipe.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        recipe_form = RestrictedRecipeForm(request.POST, request.FILES)
        if recipe_form.is_valid():
            added_recipe = recipe_form.save()
            messages.success(request, 'Successfully created and saved recipe!')
            return redirect(reverse('recipe_detail', args=[added_recipe.slug]))
        else:
            messages.error(
                request, 'Failed to add article. \
                Please ensure the form is valid.')
    else:
        recipe_form = RestrictedRecipeForm()

    template = 'blog/create_recipe.html'
    context = {'recipe_form': recipe_form}

    return render(request, template, context)


@login_required
def edit_article(request, article_id):
    """
    Edits an article on the blog - for staff only

    **Context**

    ``article``
    An instance of :model:`blog.Article`.

    ``article_form``
    :form:`RestrictedArticleForm` or `ArticleForm`

    **Template:**

    :template:`blog/edit_article.html`
    """
    if not request.user.is_staff:
        messages.error(
            request, 'Sorry, only store employees can edit a blog article.')
        return redirect(reverse('home'))

    article = get_object_or_404(Article, pk=article_id)

    if request.user.is_superuser:
        if request.method == 'POST':
            article_form = ArticleForm(
                request.POST, request.FILES, instance=article)

            if article_form.is_valid():
                edited_article = article_form.save(commit=False)
                if edited_article.approved and edited_article.date_of_publication is None:
                    messages.error(
                        request,
                        'Please make sure to set a date of publication')
                else:
                    edited_article = article_form.save()
                    messages.success(
                        request, 'Successfully updated the article')
                    return redirect(
                        reverse('article_detail', args=[edited_article.slug]))
            else:
                messages.error(
                    request, 'Failed to update article. \
                    Please ensure the form is valid.')
        else:
            article_form = ArticleForm(instance=article)
            messages.info(request, f'You are editing {article.title}')

    else:
        if request.method == 'POST':
            article_form = RestrictedArticleForm(
                request.POST, request.FILES, instance=article)

            if article_form.is_valid():
                edited_article = article_form.save(commit=False)
                edited_article.date_of_publication = None
                edited_article.approved = False
                edited_article.save()
                messages.success(request, 'Successfully updated the article')
                return redirect(
                    reverse('article_detail', args=[edited_article.slug]))
            else:
                messages.error(
                    request, 'Failed to update article. \
                    Please ensure the form is valid.')
        else:
            article_form = RestrictedArticleForm(instance=article)
            messages.info(request, f'You are editing {article.title}')

    template = 'blog/edit_article.html'
    context = {
        'article_form': article_form,
        'article': article,
    }
    return render(request, template, context)


@login_required
def edit_recipe(request, recipe_id):
    """
    Edits a recipe on the blog - for staff only

    **Context**

    ``recipe``
    An instance of :model:`blog.Recipe`.

    ``recipe_form``
    :form:`RestrictedRecipeForm` or `RecipeForm`

    **Template:**

    :template:`blog/edit_recipe.html`
    """
    if not request.user.is_staff:
        messages.error(
            request, 'Sorry, only store employees can edit a recipe.')
        return redirect(reverse('home'))

    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if request.user.is_superuser:
        if request.method == 'POST':
            recipe_form = RecipeForm(
                request.POST, request.FILES, instance=recipe)

            if recipe_form.is_valid():
                edited_recipe = recipe_form.save(commit=False)
                if edited_recipe.approved and edited_recipe.date_of_publication is None:
                    messages.error(
                        request,
                        'Please make sure to set a date of publication')
                else:
                    edited_recipe = recipe_form.save()
                    messages.success(
                        request, 'Successfully updated the recipe')
                    return redirect(
                        reverse('recipe_detail', args=[edited_recipe.slug]))
            else:
                messages.error(
                    request, 'Failed to update recipe. \
                    Please ensure the form is valid.')
        else:
            recipe_form = RecipeForm(instance=recipe)
            messages.info(request, f'You are editing {recipe.title}')

    else:
        if request.method == 'POST':
            recipe_form = RestrictedRecipeForm(
                request.POST, request.FILES, instance=recipe)

            if recipe_form.is_valid():
                edited_recipe = recipe_form.save(commit=False)
                edited_recipe.date_of_publication = None
                edited_recipe.approved = False
                edited_recipe.save()
                messages.success(request, 'Successfully updated the recipe')
                return redirect(
                    reverse('recipe_detail', args=[edited_recipe.slug]))
            else:
                messages.error(
                    request, 'Failed to update recipe. \
                    Please ensure the form is valid.')
        else:
            recipe_form = RestrictedRecipeForm(instance=recipe)
            messages.info(request, f'You are editing {recipe.title}')

    template = 'blog/edit_recipe.html'
    context = {
        'recipe_form': recipe_form,
        'recipe': recipe,
    }
    return render(request, template, context)


@login_required
def unpublish_article(request, article_id):
    """
    Unpublishes an article from the blog - for managers only
    """
    if not request.user.is_superuser:
        messages.error(
            request,
            'Sorry, only store managers can unpublish a blog article.')
        return redirect(reverse('home'))

    article = get_object_or_404(Article, pk=article_id)

    if request.method == 'POST':
        try:
            article.approved = False
            article.published = False
            article.save()
            messages.success(request, 'Article unpublished successfully.')
            return redirect(reverse('articles'))
        except Exception:
            messages.error(request, 'Sorry, the article could not be unpublished')

    template = 'blog/delete_article.html'
    context = {
        'article': article,
    }

    return render(request, template, context)


@login_required
def unpublish_recipe(request, recipe_id):
    """
    Unpublishes a recipe from the blog - for managers only
    """
    if not request.user.is_superuser:
        messages.error(
            request,
            'Sorry, only store managers can unpublish a blog recipe.')
        return redirect(reverse('home'))

    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if request.method == 'POST':
        try:
            recipe.approved = False
            recipe.published = False
            recipe.save()
            messages.success(request, 'Recipe unpublished successfully.')
            return redirect(reverse('recipes'))
        except Exception as e:
            print('Error recipe: ', e)
            messages.error(request, 'Sorry, the recipe could not be unpublished')

    template = 'blog/delete_recipe.html'
    context = {
        'recipe': recipe,
    }

    return render(request, template, context)


@login_required
def delete_article(request, article_id):
    """
    Deletes an article - for managers only

    **Context**

    ``article``
    A specific instance of :model:`blog.Article`

    **Template:**

    :template:`blog/delete_article.html`
    """

    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only store managers can delete an article.')
        return redirect(reverse('home'))

    article = get_object_or_404(Article, pk=article_id)

    if request.method == 'POST':
        try:
            article.delete()
            messages.success(request, 'Article deleted!')
            return redirect(reverse('articles'))
        except Exception:
            messages.error(request, 'Sorry, the article could not be deleted')

    template = 'blog/delete_article.html'
    context = {
        'article': article,
        'admin_delete': True,
    }

    return render(request, template, context)


@login_required
def delete_recipe(request, recipe_id):
    """
    Deletes a recipe - for managers only

    **Context**

    ``recipe``
    A specific instance of :model:`blog.Recipe`

    **Template:**

    :template:`blog/delete_recipe.html`
    """

    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only store managers can delete a recipe.')
        return redirect(reverse('home'))

    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if request.method == 'POST':
        try:
            recipe.delete()
            messages.success(request, 'Recipe deleted!')
            return redirect(reverse('recipes'))
        except Exception:
            messages.error(request, 'Sorry, the recipe could not be deleted')

    template = 'blog/delete_recipe.html'
    context = {
        'recipe': recipe,
        'admin_delete': True,
    }

    return render(request, template, context)


@login_required
def reading_list(request, slug):
    """
    Adds (1 click) or removes (double click) an article
    from an authenticated user's reading list
    """
    if request.POST and 'article_id' in request.POST:
        reading_list = Reading.objects.get(user_profile=request.user.profile)
        if 'fa-regular' in request.POST['icon_classlist_value']:
            try:
                reading_list.bookmarked_articles.add(
                    request.POST['article_id'])
                reading_list.save()
                messages.success(request, 'Article added to your reading list')
            except Exception:
                messages.error(
                    request, 'Sorry, an error occurred.Please try again later')
        elif 'fa-solid' in request.POST['icon_classlist_value']:
            try:
                reading_list.bookmarked_articles.remove(
                    request.POST['article_id'])
                reading_list.save()
                messages.success(
                    request, 'Article removed from your reading list')
            except Exception:
                messages.error(
                    request, 'Sorry, an error occurred. Please try again')
    else:
        messsages.error(
            request,
            'Sorry, something went wrong with bookmarking. Try again')

    return redirect(reverse('articles'))


@login_required
def fav_recipe_list(request, slug):
    """
    Adds (1 click) or removes (double click) a recipe
    from an authenticated user's reading list
    """
    if request.POST and 'recipe_id' in request.POST:
        fav_recipe_list = FavouriteRecipe.objects.get(
            user_profile=request.user.profile)

        if 'fa-regular' in request.POST['icon_classlist_value']:
            try:
                fav_recipe_list.bookmarked_recipes.add(
                    request.POST['recipe_id'])
                fav_recipe_list.save()
                messages.success(request, 'Recipe added to your list')
            except Exception:
                messages.error(
                    request, 'Sorry, an error occurred. Please try again')
        elif 'fa-solid' in request.POST['icon_classlist_value']:
            try:
                fav_recipe_list.bookmarked_recipes.remove(
                    request.POST['recipe_id'])
                fav_recipe_list.save()
                messages.success(request, 'Recipe removed from your list')
            except Exception:
                messages.error(
                    request, 'Sorry, an error occurred. Please try again')

    return redirect(reverse('recipes'))
