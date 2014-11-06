# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
import bsct.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('github_object', jsonfield.fields.JSONField(verbose_name=b'GitHub repository object')),
                ('name', models.CharField(max_length=100, verbose_name=b'Project name')),
                ('id', models.IntegerField(serialize=False, verbose_name=b'Repository ID', primary_key=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Repository',
                'verbose_name_plural': 'Repositories',
            },
            bases=(bsct.models.BSCTModelMixin, models.Model),
        ),
        migrations.AddField(
            model_name='project',
            name='repository',
            field=models.ForeignKey(default=None, verbose_name=b'Project GIT repository', to='projects.Repository', null=True),
            preserve_default=True,
        ),
    ]
