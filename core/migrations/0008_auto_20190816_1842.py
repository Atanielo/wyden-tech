# Generated by Django 2.2.4 on 2019-08-16 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20190816_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='arquivo',
            field=models.FileField(null=True, upload_to='arquivos'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='curso',
            field=models.CharField(max_length=20, null=True, verbose_name='curso'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='periodo',
            field=models.IntegerField(blank=True, null=True, verbose_name='periodo'),
        ),
    ]
