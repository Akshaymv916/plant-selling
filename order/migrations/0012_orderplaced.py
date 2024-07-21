# Generated by Django 5.0.7 on 2024-07-14 06:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_delete_headerimage'),
        ('order', '0011_payment'),
        ('product', '0014_alter_products_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orderplaced',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('status', models.CharField(choices=[('Accepted', 'Accepted'), ('packed', 'packed'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel'), ('Pending', 'Pending')], default='pending', max_length=50)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('payment', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='order.payment')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.customuser')),
            ],
        ),
    ]