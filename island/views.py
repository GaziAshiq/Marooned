from django.shortcuts import render
from news.models import News


# Create your views here.
def home(request):
    featured_post = News.objects.filter(status=True).order_by('-created_on')[0:3]
    return render(request, 'island/index.html', {'home': 'Welcome to Marooned', 'featured_post': featured_post})
