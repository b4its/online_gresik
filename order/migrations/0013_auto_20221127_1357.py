# Generated by Django 3.1.14 on 2022-11-27 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_order_total_harga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='catatan',
            field=models.TextField(blank=True, null=True),
        ),
    ]