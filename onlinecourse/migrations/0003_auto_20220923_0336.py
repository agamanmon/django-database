# Generated by Django 3.1.3 on 2022-09-23 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20220922_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='questionContent',
            field=models.CharField(max_length=100),
        ),
    ]
