from django.db import models
from bsct.models import BSCTModelMixin
from datetime import datetime
from jsonfield import JSONField
from django.contrib.auth.models import User
from pep8runs.models import Run


class Repository(BSCTModelMixin, models.Model):
    """ A GIT repository """

    github_object = JSONField('GitHub repository object')
    name = models.CharField(max_length=100, verbose_name='Project name')
    id = models.IntegerField('Repository ID', primary_key=True)
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return 'Repository "{}"'.format(self.name)

    bsct_list_fields = [name, owner]

    class Meta:
        verbose_name = 'Repository'
        verbose_name_plural = 'Repositories'


class Project(BSCTModelMixin, models.Model):
    """ A project """

    name = models.CharField(max_length=100, verbose_name='Project name')
    git_url_clone = models.URLField(verbose_name='URL to GIT repository')
    repository = models.ForeignKey(Repository, verbose_name='Project GIT repository', null=True, default=None)
    date_added = models.DateField(verbose_name='Date of creation', auto_now_add=True)

    def __unicode__(self):
        return 'Project "{}"'.format(self.name)

    def _get_last_problems_count(self):
        last_run = Run.objects.filter(project=self, status='ok').order_by('-time_start').first()
        return last_run.total_errors if last_run else ''
    last_problems_count = property(_get_last_problems_count)
    _get_last_problems_count.short_description = 'Last problems count'

    bsct_list_fields = [name, last_problems_count]

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
