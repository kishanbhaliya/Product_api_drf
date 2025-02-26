from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'stock_quantity', 'is_deleted')
    search_fields = ('name', 'category__name')
    list_filter = ('category', 'is_deleted')
    ordering = ('id',)

admin.site.register(Product, ProductAdmin)
