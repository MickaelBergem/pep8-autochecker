from django.db import models
from bsct.models import BSCTModelMixin
from datetime import datetime


class Project(BSCTModelMixin, models.Model):
    """ A project """

    name = models.CharField(max_length=100, verbose_name='Project name')
    git_url_clone = models.URLField(verbose_name='URL to GIT repository')
    date_added = models.DateField(verbose_name='Date of creation', auto_now_add=True)

    def __unicode__(self):
        return 'Project "{}"'.format(self.name)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
