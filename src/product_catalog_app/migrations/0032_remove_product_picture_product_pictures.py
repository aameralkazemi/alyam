# Generated by Django 4.0.1 on 2022-03-24 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_catalog_app', '0031_picture_product_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='picture',
        ),
        migrations.AddField(
            model_name='product',
            name='pictures',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product_catalog_app.picture'),
        ),
    ]
