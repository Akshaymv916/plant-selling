# Generated by Django 5.0.7 on 2024-07-13 05:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_delete_headerimage'),
        ('order', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('payable_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.customuser')),
            ],
        ),
    ]
