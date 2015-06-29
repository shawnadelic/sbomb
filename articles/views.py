from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.http import Http404
from django.template.defaultfilters import slugify
from .models import Article, Category

default_pagination = 8

class AllArticlesView(generic.ListView):
    template_name = 'articles/articles.html'
    context_object_name = 'articles'
    paginate_by = default_pagination

    def get_queryset(self):
        """ Return all articles """
        return Article.objects.filter(status=Article.PUBLISHED).order_by('-pub_date')

class ArticleView(generic.DetailView):
    template_name = 'articles/article.html'
    model = Article
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)
        return context

class CategoryView(generic.ListView):
    template_name = 'articles/category.html'
    context_object_name = 'articles_by_category'
    paginate_by = default_pagination

    def get_context_data(self, **kwargs):
        """ Get Category from objects """
        slug = self.kwargs['slug']
        context = super(CategoryView, self).get_context_data(**kwargs)
        context["category"] = get_object_or_404(Category, slug=slug)
        context["other_categories"] = Category.objects.exclude(title=context["category"])
        return context

    def get_queryset(self, **kwargs):
        """ Return articles in certain category """
        slug = self.kwargs['slug']
        return Article.objects.filter(status=Article.PUBLISHED).filter(
                categories__slug=slug).order_by('-pub_date')
