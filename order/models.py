from django.db import models

class MenuItem(models.Model):
    name = models.CharField("Название блюда", max_length=100)
    price = models.DecimalField("Цена", max_digits=6, decimal_places=2)
    description = models.TextField("Описание", blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.price} руб.)"

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В ожидании'),
        ('ready', 'Готово'),
        ('paid', 'Оплачено'),
    ]

    table_number = models.IntegerField("Номер стола")
    items = models.ManyToManyField(MenuItem, verbose_name="Список заказанных блюд")
    total_price = models.DecimalField("Общая стоимость заказа", max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField("Статус заказа", max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Order {self.id} (Table {self.table_number})"

    def calculate_total_price(self):
        self.total_price = sum(item.price for item in self.items.all())
        self.save()

