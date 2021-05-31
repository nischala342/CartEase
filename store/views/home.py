from django.shortcuts import render, redirect
from store.models.category import Category
from store.models.products import Product
from django.views import View
from store.models.subcategory import SubCategory

# Create your views here.
class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        return redirect('Homepage')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        categories = Category.get_all_categories()
        # return render(request, 'orders/order.html')
        categoryID = request.GET.get('category')
        subcategories = SubCategory.get_all_subcategories(categoryID)
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products()
        subcategoryID = request.GET.get('subcategory')
        if subcategoryID:
            products = Product.get_all_products_by_subcategoryid(subcategoryID, categoryID)
        else:
            products = Product.get_all_products()
        data = {}
        data['products'] = products
        data['categories'] = categories
        data['subcategories'] = subcategories
        # print('You are: ',request.session.get('email'))
        return render(request, 'index.html', data)










