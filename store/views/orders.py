from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.products import Product
from store.models.orders import Order
from store.middlewares.auth import auth_middleware

class OrderView(View):

    def get(self, request):
        customer = request.session.get('customer')
        order = Order.get_orders_by_customer(customer)
        #order.reverse()
        return render(request,'orders.html', {'orders': order})
