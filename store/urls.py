from django.urls import path
from .views.signup import Signup
from .views.login import Login, logout
from .views.home import Index, store
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .views.search import search
from .middlewares.auth import auth_middleware
from .views.EBuy import EBuy
from .views.feedback import  Feedback


urlpatterns = [
    path('', EBuy.as_view(), name='Homepage'),
    path('home', Index.as_view(), name='home'),
    path('store', store, name='store'),
    path('signup',Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()), name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='order'),
    path('search',search,name='search'),
    path('feedback', Feedback.as_view(), name='feedback'),
]
