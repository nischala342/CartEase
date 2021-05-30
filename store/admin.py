from django.contrib import admin
from .models.products import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from .models.subcategory import SubCategory

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','category']
class AdminCategory(admin.ModelAdmin):
    list_display = ['name']
class AdminSubCategory(admin.ModelAdmin):
    list_display = ['name']
# Register your models here.
admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(SubCategory,AdminSubCategory)
admin.site.register(Customer)
admin.site.register(Order)

