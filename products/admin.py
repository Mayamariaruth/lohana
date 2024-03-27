from django.contrib import admin
from .models import Product, Category, Review
from django_summernote.admin import SummernoteModelAdmin


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
