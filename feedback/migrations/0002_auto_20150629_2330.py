# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name_plural': 'Feedback'},
        ),
        migrations.AddField(
            model_name='feedback',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 29, 23, 30, 20, 349102, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
