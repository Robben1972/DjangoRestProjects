from django.urls import path
from .views import ProductList, CategoryList, OrderList, OrderItemList, ProductDetail, CategoryDetail, OrderListEach, \
    OrderItemListDetail

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('orders/', OrderList, name='order-list'),
    path('orders/<int:pk>/', OrderListEach, name='order-list'),
    path('order-items/', OrderItemList.as_view(), name='order-item-list'),
    path('order-items/<int:pk>/', OrderItemListDetail, name='order-item-list'),
]
