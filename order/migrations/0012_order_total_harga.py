# Generated by Django 3.1.14 on 2022-11-27 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_auto_20221125_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_harga',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
