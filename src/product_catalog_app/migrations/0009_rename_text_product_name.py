# Generated by Django 4.0.1 on 2022-02-02 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_catalog_app', '0008_alter_category_options_alter_subcategory_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='text',
            new_name='name',
        ),
    ]
