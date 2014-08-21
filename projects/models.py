from django.db import models
from bsct.models import BSCTModelMixin
from datetime import datetime


class Project(BSCTModelMixin, models.Model):
    """ A project """

    name = models.TextField(verbose_name='Project name')
    git_url_clone = models.URLField(verbose_name='URL to GIT repository')
    date_added = models.DateField(verbose_name='Date of creation', default=datetime.now())

    def __unicode__(self):
        return "Project '%s'".format(self.name)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
