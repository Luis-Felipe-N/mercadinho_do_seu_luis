# Generated by Django 4.0.3 on 2022-04-02 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='perfil_imagem',
            field=models.ImageField(null=True, upload_to='users/perfil/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='vendedor',
            name='telefone',
            field=models.CharField(max_length=11, verbose_name='Telefone'),
        ),
    ]
