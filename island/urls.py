from django.urls import path
from .views import home

app_name = 'island'
urlpatterns = [
    path('', home, name='home'),
]
