from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from order.forms import MenuItemForm, OrderForm
from order.models import MenuItem, Order


def menu_list(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu/menu_list.html', {'menu_items': menu_items})

def menu_item_create(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuItemForm()
    return render(request, 'menu/menu_item_form.html', {'form': form})

def menu_item_update(request, item_id):
    menu_item = get_object_or_404(MenuItem, id=item_id)
    if request.method == 'POST':
        form = MenuItemForm(request.POST, instance=menu_item)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuItemForm(instance=menu_item)
    return render(request, 'menu/menu_item_form.html', {'form': form})

def menu_item_delete(request, item_id):
    menu_item = get_object_or_404(MenuItem, id=item_id)
    if request.method == 'POST':
        menu_item.delete()
        return redirect('menu_list')
    return render(request, 'menu/menu_item_confirm_delete.html', {'menu_item': menu_item})

# Views for Orders
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})

def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/order_detail.html', {'orders': order})

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            form.save_m2m()
            order.calculate_total_price()
            return redirect('order_detail', order_id=order.id)
    else:
        form = OrderForm()
    return render(request, 'orders/order_form.html', {'form': form})

def order_update(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            form.save_m2m()
            order.calculate_total_price()
            return redirect('order_detail', order_id=order.id)
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/order_form.html', {'form': form})

def order_delete(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'orders/order_confirm_delete.html', {'orders': order})


from django.db.models import Sum

def revenue_report(request):
    revenue = Order.objects.filter(status='paid').aggregate(total_revenue=Sum('total_price'))['total_revenue'] or 0.00
    return render(request, 'orders/revenue_report.html', {'revenue': revenue})
