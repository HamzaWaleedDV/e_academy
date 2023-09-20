from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Article, Category
from .froms import ArticleForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'create.html'
    success_url = reverse_lazy('article_view')


class ArticleListView(ListView):
    model = Article
    template_name = 'blog.html'
    context_object_name = 'articles'
    paginate_by = 12
    queryset = Article.objects.select_related('category')


    def get_queryset(self):
        query_set = super().get_queryset()
        where = []
        q = self.request.GET.get('q', None)
        cid = self.kwargs.get('id')
        
        if q:
            where.append(Q(title__icontains=q))
        if cid:
            where.append(Q(category_id=cid))

        if where:
            from functools import reduce
            from operator import or_

            query_set = query_set.filter(reduce(or_, where))

        return query_set
    

class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'art'
    template_name = 'single.html'


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'update.html'
    success_url = reverse_lazy('article_view')


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'delete.html'
    context_object_name = 'article'
    success_url = reverse_lazy('article_view')
