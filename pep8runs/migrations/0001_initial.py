# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
import bsct.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PEP8Message',
            fields=[
                ('code', models.CharField(max_length=4, serialize=False, verbose_name=b'Code', primary_key=True)),
                ('message', models.TextField(verbose_name=b'Message')),
            ],
            options={
                'verbose_name': 'PEP8 error / warning',
                'verbose_name_plural': 'PEP8 errors / warnings',
            },
            bases=(bsct.models.BSCTModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_start', models.DateTimeField(auto_now_add=True, verbose_name=b'Date of run start')),
                ('finished', models.BooleanField(default=False, verbose_name=b'Run finished')),
                ('duration', models.DecimalField(default=0, verbose_name=b'Run duration', max_digits=8, decimal_places=2)),
                ('status', models.CharField(default=b'unknown', max_length=10, verbose_name=b'Run status', choices=[(b'ok', b'ok'), (b'err', b'err'), (b'unknown', b'unknown')])),
                ('raw_output', models.TextField(verbose_name=b'Raw output')),
                ('counters', jsonfield.fields.JSONField(verbose_name=b'Counters')),
                ('total_errors', models.IntegerField(verbose_name=b'Total errors')),
                ('project', models.ForeignKey(verbose_name=b'Project', to='projects.Project')),
            ],
            options={
                'verbose_name': 'PEP8 run',
                'verbose_name_plural': 'PEP8 runs',
            },
            bases=(bsct.models.BSCTModelMixin, models.Model),
        ),
    ]
