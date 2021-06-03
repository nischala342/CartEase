from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.views import View

from store.models.customer import Customer


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        value = {
            'first_name': first_name, 'last_name': last_name
            , 'phone': phone, 'email': email
        }
        error_message = None
        customer = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password)
        # validation
        error_message = self.validateCustomer(customer)
        # saving
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()

            return redirect('store')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if not customer.first_name:
            error_message = "First Name Required !"
        elif len(customer.first_name) < 4:
            error_message = "first name must have more than 4 characters!!"
        elif not customer.last_name:
            error_message = "Last Name Required !"
        elif len(customer.last_name) < 4:
            error_message = "Last name must have more than 4 characters!!"
        elif not customer.phone:
            error_message = "Phone Number required!!"
        elif len(customer.phone) < 10:
            error_message = "Phone Number must have 10 digits!"
        elif len(customer.password) < 8:
            error_message = "password must be 8 characters long"
        elif customer.isExists():
            error_message = 'Email Address already registered'
        return error_message
