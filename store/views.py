from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models.category import Category
from .models.customer import Customer
from .models.products import Product
from django.views import View


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

def validateCustomer(customer):
    error_message= None
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

def registerUser(request):
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
        error_message = validateCustomer(customer)
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

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        return registerUser(request)

class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                return redirect('Homepage')
            else:
                error_message = 'Email or Password invalid!!'
        else:
            error_message = 'Email or Password invalid!!'
        return render(request, 'login.html', {'error': error_message})



