# Generated by Django 3.1.14 on 2022-11-27 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_auto_20221113_1454'),
        ('order', '0013_auto_20221127_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Alamat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alamat', to='payment.billingaddress'),
        ),
    ]
