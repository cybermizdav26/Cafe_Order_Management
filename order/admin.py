from django.contrib import admin

from order.models import Order, MenuItem

admin.site.register(Order)
admin.site.register(MenuItem)
