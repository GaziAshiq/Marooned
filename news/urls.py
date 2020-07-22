from django.urls import path
from .views import NewsList, NewsDetail, TagList

app_name = 'news'
urlpatterns = [
    path('', NewsList.as_view(), name='news'),
    path('tags/', TagList.as_view(), name='tags'),
    path('<slug:slug>/', NewsDetail.as_view(), name='post'),
]
