# Generated by Django 3.0.3 on 2020-07-07 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='cover_photo',
            field=models.ImageField(blank=True, height_field='avatar_height', null=True, upload_to='', width_field='avatar_width'),
        ),
    ]