# Generated by Django 3.0.6 on 2020-08-23 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_post_author_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author_image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]