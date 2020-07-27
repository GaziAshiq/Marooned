from .models import News, Tag
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import NewsPublishForm


# Create your views here.
class NewsListView(ListView):
    queryset = News.objects.filter(status=1).order_by('-created_on')
    context_object_name = 'news_list'
    paginate_by = 2


class NewsDetailView(DetailView):
    model = News
    context_object_name = 'post'


class NewsCreateView(LoginRequiredMixin, CreateView):
    # model = News
    # fields = ['title', 'slug', 'cover_photo', 'summary', 'content', 'tags']

    # using form_class so i can use summernote
    form_class = NewsPublishForm
    template_name = 'news/news_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(NewsCreateView, self).form_valid(form)


class NewsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News

    form_class = NewsPublishForm
    template_name = 'news/news_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(NewsUpdateView, self).form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class NewsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/news/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class TagListView(ListView):
    queryset = Tag.objects.all()
    template_name = 'news/tags.html'
    context_object_name = 'tag_list'
