# Generated by Django 3.1.14 on 2023-03-25 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_clients_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]