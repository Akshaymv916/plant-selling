# Generated by Django 5.0.7 on 2024-07-16 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0031_remove_order_payment_checkout_paymentmode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='paymentmode',
            field=models.CharField(default='Cash on delivery', max_length=20),
        ),
    ]