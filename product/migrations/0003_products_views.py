# Generated by Django 5.0.7 on 2024-07-11 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_products_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
