# Generated by Django 4.0 on 2023-04-09 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promocodes', '0004_alter_promocodes_options_remove_promocodes_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='promocodes',
            name='amount',
            field=models.PositiveIntegerField(default=0, verbose_name='Amount'),
        ),
    ]
