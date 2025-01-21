from django_filters import filters, FilterSet

from order.models import Order


class OrderFilter(FilterSet):
    table_number = filters.NumberFilter(field_name="table_number", lookup_expr='exact')
    status = filters.CharFilter(field_name="status", lookup_expr='icontains')

    class Meta:
        model = Order
        fields = ['table_number', 'status']
