# Generated by Django 2.2.12 on 2020-08-09 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_cage_diff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cage',
            name='diff',
            field=models.CharField(default='lol', max_length=100),
        ),
    ]
