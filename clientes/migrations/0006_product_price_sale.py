# Generated by Django 4.0.5 on 2022-07-21 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_person_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clientes.person')),
                ('products', models.ManyToManyField(to='clientes.product')),
            ],
        ),
    ]
