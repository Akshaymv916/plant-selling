# Generated by Django 5.0.7 on 2024-07-13 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_order_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.TextField(default=0),
        ),
    ]
