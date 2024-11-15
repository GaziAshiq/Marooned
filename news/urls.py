from django.urls import path
from .views import (NewsListView, NewsDetailView, NewsCreateView, NewsUpdateView, NewsDeleteView,
                    UserPostListView, TagListView, tag_detail)

app_name = 'news'
urlpatterns = [
    path('', NewsListView.as_view(), name='news'),
    path('author/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('new/', NewsCreateView.as_view(), name='news-create'),
    path('tags/', TagListView.as_view(), name='tags'),
    path('tags/<slug:slug>/', tag_detail, name='tag-detail'),
    path('<slug:slug>/', NewsDetailView.as_view(), name='post'),
    path('<slug:slug>/update/', NewsUpdateView.as_view(), name='news-update'),
    path('<slug:slug>/delete/', NewsDeleteView.as_view(), name='news-delete'),
]
