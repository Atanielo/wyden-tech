# Generated by Django 2.2.4 on 2019-08-18 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20190818_1537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidato',
            name='arquivo',
        ),
    ]
