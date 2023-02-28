from django.contrib import admin

from webapp.models import Product


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'remainder', 'name', 'description', 'category', 'price')
    list_filter = ('id', 'remainder', 'name', 'description', 'category', 'price')
    search_fields = ('remainder', 'name', 'description', 'price')
    fields = ('remainder', 'name', 'description', 'category', 'price')
    readonly_fields = ('id', 'price', 'remainder')


admin.site.register(Product, ProductAdmin)
