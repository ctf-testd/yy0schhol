# Generated by Django 3.2.18 on 2023-04-13 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0008_alter_clients_options_alter_clients_balance_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients',
            name='status',
        ),
    ]
