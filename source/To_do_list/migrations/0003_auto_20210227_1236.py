# Generated by Django 3.1.7 on 2021-02-27 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('To_do_list', '0002_auto_20210227_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Описание'),
        ),
    ]
