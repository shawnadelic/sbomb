# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('status', models.IntegerField(default=0, choices=[(0, b'Draft'), (1, b'Submitted'), (2, b'Published')])),
                ('author', models.ForeignKey(related_name='article_author', to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, db_index=True)),
                ('slug', models.SlugField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(to='articles.Category'),
        ),
        migrations.AddField(
            model_name='article',
            name='editor',
            field=models.ForeignKey(related_name='article_editor', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
