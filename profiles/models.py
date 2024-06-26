from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django_countries.fields import CountryField
from products.models import Product


# Create your models here.
class UserProfile(models.Model):
    """
    User profile model
    Save user delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_phone_number = models.CharField(max_length=20, null=True, blank=True)
    user_street_address1 = models.CharField(
        max_length=80, null=True, blank=True
    )
    user_street_address2 = models.CharField(
        max_length=80, null=True, blank=True
    )
    user_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    user_county = models.CharField(max_length=80, null=True, blank=True)
    user_postcode = models.CharField(max_length=20, null=True, blank=True)
    user_country = CountryField(blank_label='Country', null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()


class WishlistItem(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='wishlist_items'
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f'{self.user.username} - {self.product.name}'
