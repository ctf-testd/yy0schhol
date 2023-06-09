# Generated by Django 4.0 on 2023-04-08 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0005_remove_clients_login_clients_email'),
        ('products', '0003_alter_products_id_alter_productscategories_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('status', models.CharField(choices=[('in_processing', 'IN_PROCESSING'), ('processed', 'PROCESSED')], max_length=255, verbose_name='Status')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clients.clients', verbose_name='Client')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='OrderProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.orders', verbose_name='Order product')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Order product',
                'verbose_name_plural': 'Order products',
            },
        ),
    ]
