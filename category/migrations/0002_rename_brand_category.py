# Generated by Django 5.0.7 on 2024-07-11 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Brand',
            new_name='Category',
        ),
    ]