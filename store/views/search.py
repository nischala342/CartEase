from django.shortcuts import render
from store.models.products import Product
def search(request):
    query = None
    products = []
    if request.method == "GET":
        query =  (request.GET.get('query')).lower()
        products = Product.get_all_products()
        #print(query,products[0].name)
        product_names = [(product.name).lower() for product in products]
        zip_object = zip(products, product_names)
    return render(request, 'search.html',{'query':query,'zip_object':zip_object})