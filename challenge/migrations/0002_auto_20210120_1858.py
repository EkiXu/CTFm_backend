# Generated by Django 3.1.5 on 2021-01-20 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challengecategory',
            name='icon',
            field=models.CharField(default='', max_length=64),
        ),
    ]
