# Generated by Django 2.2.12 on 2020-08-09 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_cage2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cage2',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
