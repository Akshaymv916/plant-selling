# Generated by Django 5.0.7 on 2024-07-14 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_products_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='stock',
            field=models.CharField(choices=[('IN_STOCK', 'IN_STOCK'), ('OUT_OF_STOCK', 'OUT_OF_STOCK')], max_length=30),
        ),
    ]
