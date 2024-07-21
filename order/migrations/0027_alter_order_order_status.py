# Generated by Django 5.0.7 on 2024-07-15 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0026_alter_order_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.IntegerField(choices=[(1, 'ORDER_CONFIRMED'), (2, 'ORDER_SHIPPED'), (3, 'ORDER_DELIVERED'), (4, 'ORDER_REJECTED')], default=0),
        ),
    ]
