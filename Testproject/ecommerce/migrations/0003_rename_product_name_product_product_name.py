# Generated by Django 5.2.3 on 2025-06-29 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_rename_name_product_product_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Product_name',
            new_name='product_name',
        ),
    ]
