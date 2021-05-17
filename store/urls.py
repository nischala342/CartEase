from django.urls import path
from .views.signup import Signup
from .views.login import Login
from .views.home import Index



urlpatterns = [
    path('', Index.as_view(), name='Homepage'),
    path('signup',Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login')
]
