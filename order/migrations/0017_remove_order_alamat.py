# Generated by Django 3.1.14 on 2022-11-27 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0016_order_alamat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='Alamat',
        ),
    ]
