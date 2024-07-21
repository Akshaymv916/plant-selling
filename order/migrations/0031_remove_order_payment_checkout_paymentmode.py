# Generated by Django 5.0.7 on 2024-07-16 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0030_alter_order_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment',
        ),
        migrations.AddField(
            model_name='checkout',
            name='paymentmode',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
