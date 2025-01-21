from django import forms

from order.models import Order, MenuItem


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['table_number', 'items', 'status']
        widgets = {
            'items': forms.CheckboxSelectMultiple(),
            'status': forms.Select(choices=Order.STATUS_CHOICES),
        }

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'price', 'description']

