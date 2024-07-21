# Generated by Django 5.0.7 on 2024-07-12 10:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_product_review_review_desp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_review',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='product.products'),
        ),
    ]