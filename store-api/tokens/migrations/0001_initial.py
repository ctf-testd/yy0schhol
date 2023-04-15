# Generated by Django 4.0 on 2023-04-08 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0004_alter_clients_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='RefreshTokens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=255, verbose_name='Токен')),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='clients.clients', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Refresh Токен',
                'verbose_name_plural': 'Refresh Токены',
            },
        ),
    ]
