# Generated by Django 3.2.8 on 2021-11-29 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vouchers', '0004_alter_voucher_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voucher',
            name='product',
        ),
    ]
