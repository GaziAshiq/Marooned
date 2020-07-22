from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import signup, profile

app_name = 'users'
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', LoginView.as_view(template_name='users/signin.html'), name='signin'),
    path('signout/', LogoutView.as_view(template_name='users/signout.html'), name='signout'),
    path('profile/', profile, name='profile')
]
