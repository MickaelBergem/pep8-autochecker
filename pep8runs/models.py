from django.db import models
from bsct.models import BSCTModelMixin
from datetime import datetime

from projects.models import Project


class Run(BSCTModelMixin, models.Model):
    """ A PEP8 run on a project """

    STATUS_CHOICES = [
        ('ok', 'ok'),
        ('err', 'err'),
        ('unknown', 'unknown'),
    ]

    project = models.ForeignKey(Project, verbose_name='Project')
    time_start = models.DateTimeField(default=datetime.now(),
                                      verbose_name='Date of run start')
    finished = models.BooleanField(verbose_name='Run finished')
    duration = models.IntegerField(verbose_name='Run duration')
    status = models.CharField(verbose_name='Run status',
                              max_length=10,
                              choices=STATUS_CHOICES,
                              default='unknown')
    raw_output = models.TextField(verbose_name='Raw output')

    bsct_list_fields = [project, time_start, finished, duration]

    def __unicode__(self):
        return "Run for {} at {}".format(self.project.name, self.time_start)

    def duration_detail(self):
        return "{} s".format(self.duration)

    def finished_detail(self):
        return "Finished" if self.finished else "Still running..."

    class Meta:
        verbose_name = "PEP8 run"
        verbose_name_plural = "PEP8 runs"
