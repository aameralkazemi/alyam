# Generated by Django 4.0.1 on 2022-02-02 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_catalog_app', '0005_category_alter_product_photo_subcategory_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]
