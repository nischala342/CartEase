from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from store.models.customer import Customer
from django.views import View
from store.models.products import Product
from store.models.orders import Order
from store.views.sendemail import send_email

class CheckOut(View):

    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))

        for product in products:
            order = Order(customer=Customer(id=customer), product=product, price=product.price, address=address,
                          phone=phone, quantity=cart.get(str(product.id)))
            order.placeOrder()
            #send_email(email,"Order Placed Successfully","Regarding your EBuy Order")
        request.session['cart'] = {}

        return redirect('cart')
