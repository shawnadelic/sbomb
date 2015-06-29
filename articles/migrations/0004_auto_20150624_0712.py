# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20150624_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(related_name='article_author', default=None, blank=True, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='editor',
            field=models.ForeignKey(related_name='article_editor', default=None, blank=True, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
