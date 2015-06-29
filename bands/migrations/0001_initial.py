# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('website', models.URLField(null=True)),
                ('bandcamp', models.URLField(null=True)),
                ('facebook', models.URLField(null=True)),
                ('twitter', models.URLField(null=True)),
                ('image', models.ImageField(null=True, upload_to=b'articles/%Y/%m/%d')),
                ('description', models.TextField(null=True)),
                ('bio', models.TextField(null=True)),
            ],
        ),
    ]
