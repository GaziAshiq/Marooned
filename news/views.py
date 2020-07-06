from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Tag
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin


# Create your views here.
class TagList(ListView):
    queryset = Tag.objects.all()
    template_name = 'news/tags.html'
    context_object_name = 'tag_list'


class NewsList(ListView):
    queryset = News.objects.filter(status=1).order_by('-created_on')
    template_name = 'news/blog.html'
    context_object_name = 'news_list'
    paginate_by = 2


class NewsDetail(DetailView):
    model = News
    template_name = 'news/post.html'
    context_object_name = 'post'
