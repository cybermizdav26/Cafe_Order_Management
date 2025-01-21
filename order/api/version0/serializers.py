from rest_framework import serializers

from ...models import MenuItem, Order

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'


class OrderCreateSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(queryset=MenuItem.objects.all(), many=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['table_number', 'items', 'total_price', 'status']

    def get_total_price(self, obj):
        obj.calculate_total_price()
        return obj.total_price

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        order.items.set(items_data)
        order.save()
        return order


class OrderDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id']


class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status']


class OrderListSerializer(serializers.ModelSerializer):
    items = serializers.StringRelatedField(many=True)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Order
        fields = ['id', 'table_number', 'items', 'total_price', 'status']


class RevenueSerializer(serializers.Serializer):
    total_revenue = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        fields = ['total_revenue']


