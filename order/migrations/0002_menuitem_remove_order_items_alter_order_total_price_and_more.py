# Generated by Django 5.1.5 on 2025-01-21 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название блюда')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Цена')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
        ),
        migrations.RemoveField(
            model_name='orders',
            name='items',
        ),
        migrations.AlterField(
            model_name='orders',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Общая стоимость заказа'),
        ),
        migrations.AddField(
            model_name='orders',
            name='items',
            field=models.ManyToManyField(to='orders.menuitem', verbose_name='Список заказанных блюд'),
        ),
    ]
