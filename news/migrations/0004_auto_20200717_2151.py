# Generated by Django 3.0.3 on 2020-07-17 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20200717_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]