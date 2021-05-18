from django.urls import path
from .views.signup import Signup
from .views.login import Login, logout
from .views.home import Index
from .views.cart import Cart



urlpatterns = [
    path('', Index.as_view(), name='Homepage'),
    path('signup',Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', Cart.as_view() , name='cart')
]
