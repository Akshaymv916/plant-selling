# Generated by Django 5.0.7 on 2024-07-12 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_products_image2_alter_products_image3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='desc',
            field=models.TextField(default=True),
        ),
    ]