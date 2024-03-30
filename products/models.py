from django.db import models
from django_summernote.fields import SummernoteTextField
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    introduction = models.CharField(max_length=200, null=True, blank=True)
    description = SummernoteTextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    review_name = models.CharField(max_length=100)
    review_text = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.review_name} on {self.product}"
