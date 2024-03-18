from django.contrib import admin
from .models import Product, Category


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'sku',
        'name',
        'price',
        'image',
    )

    ordering = ('sku', 'category', 'name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
