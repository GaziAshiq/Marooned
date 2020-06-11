from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'island/index.html', {'home': 'Welcome to Marooned'})
