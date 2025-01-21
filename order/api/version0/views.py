from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, CreateAPIView, get_object_or_404, DestroyAPIView, UpdateAPIView, \
    GenericAPIView
from rest_framework.response import Response

from .filters import OrderFilter
from .serializers import (
    OrderListSerializer,
    OrderUpdateSerializer,
    RevenueSerializer, MenuItemSerializer, OrderCreateSerializer
)
from ...models import Order, MenuItem


class MenuCreateApiView(CreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class MenuListApiView(ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer


class OrderDeleteAPIView(DestroyAPIView):
    queryset = Order.objects.all()

    def delete(self, request, pk):
        recipe = get_object_or_404(Order, pk=pk)
        self.check_object_permissions(self.request, recipe)
        self.perform_destroy(recipe)
        return Response({'message': 'Order deleted successfully .'})


class OrderUpdateApiView(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderUpdateSerializer

class OrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer


class RevenueAPIView(GenericAPIView):
    serializer_class = RevenueSerializer

    def get(self, request):
        total_revenue = Order.objects.filter(status='paid').aggregate(total_revenue=Sum('total_price'))['total_revenue'] or 0
        data = {'total_revenue': total_revenue}
        return Response(data, status=status.HTTP_200_OK)

class OrderSearchAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    filterset_class = OrderFilter
    ordering_fields = ['status', 'table_number']



