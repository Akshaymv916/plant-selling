# Generated by Django 5.0.7 on 2024-07-17 06:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0034_orderitem_item_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.order'),
        ),
    ]