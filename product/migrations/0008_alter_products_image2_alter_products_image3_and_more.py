# Generated by Django 5.0.7 on 2024-07-12 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_products_image2_alter_products_image3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image2',
            field=models.ImageField(default=True, null=True, upload_to='product_images'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image3',
            field=models.ImageField(default=True, null=True, upload_to='product_images'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image4',
            field=models.ImageField(default=True, null=True, upload_to='product_images'),
        ),
    ]