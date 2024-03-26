from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products, name="products"),
    path('<int:product_id>/', views.product_detail, name="product_detail"),
    path('admin_products/', views.admin_products, name="admin_products"),
]
