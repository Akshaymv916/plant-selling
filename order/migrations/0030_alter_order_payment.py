# Generated by Django 5.0.7 on 2024-07-16 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0029_orderitem_delivery_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
