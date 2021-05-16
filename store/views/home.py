from django.shortcuts import render, redirect
from store.models.category import Category
from store.models.products import Product


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
    # print('You are: ',request.session.get('email'))
    return render(request, 'index.html', data)









