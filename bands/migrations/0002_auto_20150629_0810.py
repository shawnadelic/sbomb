# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='bandcamp',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='band',
            name='bio',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='band',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='band',
            name='email',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='band',
            name='facebook',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='band',
            name='image',
            field=models.ImageField(null=True, upload_to=b'articles/%Y/%m/%d', blank=True),
        ),
        migrations.AlterField(
            model_name='band',
            name='twitter',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='band',
            name='website',
            field=models.URLField(null=True, blank=True),
        ),
    ]
