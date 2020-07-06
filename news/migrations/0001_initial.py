# Generated by Django 3.0.3 on 2020-07-06 04:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=64, unique=True)),
                ('tag_slug', models.SlugField(max_length=64, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=192, unique=True)),
                ('slug', models.SlugField(max_length=192, unique=True)),
                ('cover_photo', models.ImageField(blank=True, height_field='avatar_height', null=True, upload_to='News', width_field='avatar_width')),
                ('avatar_height', models.IntegerField(blank=True, default='628', null=True)),
                ('avatar_width', models.IntegerField(blank=True, default='1200', null=True)),
                ('summary', models.CharField(max_length=280)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_author', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, related_name='post_tag', to='news.Tag')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
