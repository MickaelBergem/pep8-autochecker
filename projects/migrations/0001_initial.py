# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import bsct.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Project name')),
                ('git_url_clone', models.URLField(verbose_name=b'URL to GIT repository')),
                ('date_added', models.DateField(auto_now_add=True, verbose_name=b'Date of creation')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
            bases=(bsct.models.BSCTModelMixin, models.Model),
        ),
    ]
