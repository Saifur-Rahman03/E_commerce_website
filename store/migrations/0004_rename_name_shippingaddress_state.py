# Generated by Django 3.2.9 on 2021-12-09 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='name',
            new_name='state',
        ),
    ]