# Generated by Django 2.2.4 on 2019-08-18 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_candidato_arquivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='email',
            field=models.EmailField(max_length=40, unique=True, verbose_name='email'),
        ),
    ]
