# Generated by Django 4.0.3 on 2022-04-16 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercado', '0007_carrinho'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrinho',
            name='quantidade',
            field=models.IntegerField(default=1, verbose_name='Quantidade'),
        ),
    ]