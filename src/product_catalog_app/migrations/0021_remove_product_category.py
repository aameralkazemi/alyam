# Generated by Django 4.0.1 on 2022-02-23 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_catalog_app', '0020_delete_subcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
