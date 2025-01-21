from django.urls import path

from order.views import (
    order_list, order_create,
    order_detail, order_update,
    order_delete, menu_item_delete,
    menu_item_create, menu_list,
    menu_item_update, revenue_report
)

urlpatterns = [
    # Orders
    path('', order_list, name='order_list'),
    path('<int:order_id>/', order_detail, name='order_detail'),
    path('create/', order_create, name='order_create'),
    path('<int:order_id>/edit/', order_update, name='order_update'),
    path('<int:order_id>/delete/', order_delete, name='order_delete'),
    # Menu
    path('menu/', menu_list, name='menu_list'),
    path('menu/create/', menu_item_create, name='menu_item_create'),
    path('menu/<int:item_id>/edit/', menu_item_update, name='menu_item_update'),
    path('menu/<int:item_id>/delete/', menu_item_delete, name='menu_item_delete'),
    path('revenue/', revenue_report, name='revenue_report'),
]