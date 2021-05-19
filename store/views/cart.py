from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from store.models.customer import Customer
from django.views import View
from store.models.products import Product
class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)

        return render(request, 'cart.html', {'products' : products})
