from django.urls import path
from . import views
from products.views import add_to_wishlist


urlpatterns = [
    path('', views.profile, name="profile"),
    path('order_history/<order_number>/', views.order_history, name="order_history"),
    path('add_to_wishlist/', add_to_wishlist, name="add_to_wishlist_profile"),
]
