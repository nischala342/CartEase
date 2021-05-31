from django.shortcuts import render
from store.models.products import Product
def search(request):
    query = None
    products = []
    if request.method == "GET":
        query = request.GET.get('query')
        products = Product.get_all_products()
        #print(query,products[0].name)
    return render(request, 'search.html',{'query':query,'products':products})