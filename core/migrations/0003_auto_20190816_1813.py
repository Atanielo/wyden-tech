# Generated by Django 2.2.4 on 2019-08-16 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190816_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='celular',
            field=models.CharField(default='', editable=False, max_length=15, verbose_name='celular'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='data_nascimento',
            field=models.DateField(null=True),
        ),
    ]
