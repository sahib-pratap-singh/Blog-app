# Generated by Django 3.0.6 on 2020-08-23 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='update',
            field=models.DateField(auto_now=True),
        ),
    ]
