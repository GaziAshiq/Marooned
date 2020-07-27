from django.urls import path
from .views import NewsListView, NewsDetailView, NewsCreateView, NewsUpdateView, NewsDeleteView, TagListView

app_name = 'news'
urlpatterns = [
    path('', NewsListView.as_view(), name='news'),
    path('new/', NewsCreateView.as_view(), name='news-create'),
    path('tags/', TagListView.as_view(), name='tags'),
    path('<slug:slug>/', NewsDetailView.as_view(), name='post'),
    path('<slug:slug>/update/', NewsUpdateView.as_view(), name='news-update'),
    path('<slug:slug>/delete/', NewsDeleteView.as_view(), name='news-delete'),
]
