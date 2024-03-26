from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products, name="products"),
    path('<int:product_id>/', views.product_detail, name="product_detail"),
    path('add/', views.add_products, name="add_products"),
    path('edit/<int:product_id>/', views.edit_products, name="edit_products"),
]
