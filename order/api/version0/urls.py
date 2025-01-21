from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    OrderListAPIView,
    MenuCreateApiView,
    OrderDeleteAPIView,
    OrderUpdateApiView,
    RevenueAPIView,
    OrderSearchAPIView,
    MenuListApiView,
    OrderCreateAPIView
)

urlpatterns = [
    path('orders/', OrderListAPIView.as_view(), name='list'),
    path('menu-create/', MenuCreateApiView.as_view(), name='menu-create'),
    path('menu/', MenuListApiView.as_view(), name='menu-list'),
    path('order-create/', OrderCreateAPIView.as_view(), name='order-create'),
    path('order-delete<int:pk>', OrderDeleteAPIView.as_view(), name='order-delete'),
    path('order-update<int:pk>', OrderUpdateApiView.as_view(), name='order-update'),
    path('revenue/', RevenueAPIView.as_view(), name='revenue'),
    path('orders-search/', OrderSearchAPIView.as_view(), name='order-search'),
]
