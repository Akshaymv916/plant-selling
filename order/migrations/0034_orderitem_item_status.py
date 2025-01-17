# Generated by Django 5.0.7 on 2024-07-16 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0033_remove_cancelorder_email_remove_cancelorder_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='item_status',
            field=models.IntegerField(choices=[(1, 'ORDER_CONFIRMED'), (2, 'ORDER_SHIPPED'), (3, 'ORDER_DELIVERED'), (4, 'ORDER_REJECTED')], default=1),
        ),
    ]
