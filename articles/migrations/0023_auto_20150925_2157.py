# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0022_auto_20150921_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to=b'articles/%Y/%m/%d', null=True, verbose_name=b'Header Image', blank=True),
        ),
    ]
