# Generated by Django 4.0.5 on 2022-07-22 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0007_sale_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='product',
        ),
    ]
