
from django.contrib import admin
from django.urls import path
from .views import index, signup, Login
urlpatterns = [
    path('', index , name = 'Homepage'),
    path('signup', signup ),
    path('login', Login.as_view)
]
