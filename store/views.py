from django.shortcuts import render
from  django.http import HttpResponse
from .models.products import Product
from .models.category import Category

# Create your views here.
def index(request):
    products = None
    categories = Category.get_all_categories()
    #return render(request, 'orders/order.html')
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()

    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request,'index.html',data)



def signup(request):
    if request.method == 'GET' :
        return render(request, 'signup.html')
    else:
        return HttpResponse(request.POST.get('email'))
