# Generated by Django 3.0.6 on 2020-08-22 15:54

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('content', ckeditor.fields.RichTextField()),
                ('update', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-timestamp', '-update'],
            },
        ),
    ]
