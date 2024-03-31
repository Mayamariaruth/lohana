from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Product, Category, Review


# Register your models here.
class ProductAdmin(SummernoteModelAdmin):
    list_display = (
        'category',
        'sku',
        'name',
        'price',
        'image',
    )

    ordering = ('sku', 'category', 'name',)
    summernote_fields = ('description',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Review)
