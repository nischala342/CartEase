from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models.category import Category
from .models.customer import Customer
from .models.products import Product


# Create your views here.
def index(request):
    products = None
    categories = Category.get_all_categories()
    # return render(request, 'orders/order.html')
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()

    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request, 'index.html', data)


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        # validation
        value = {
            'first_name': first_name, 'last_name': last_name
            , 'phone': phone, 'email': email
        }
        error_message = None
        customer = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password)
        if not first_name:
            error_message = "First Name Required !"
        elif len(first_name) < 4:
            error_message = "first name must have more than 4 characters!!"
        elif not last_name:
            error_message = "Last Name Required !"
        elif len(last_name) < 4:
            error_message = "Last name must have more than 4 characters!!"
        elif not phone:
            error_message = "Phone Number required!!"
        elif len(phone) < 10:
            error_message = "Phone Number must have 10 digits!"
        elif len(password) < 8:
            error_message = "password must be 8 characters long"
        elif customer.isExists():
            error_message = 'Email Address already registered'
        # saving
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()

            return redirect('Homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)
