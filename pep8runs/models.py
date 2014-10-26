from django.db import models
from bsct.models import BSCTModelMixin
from django.utils import timezone
from jsonfield import JSONField


class Run(BSCTModelMixin, models.Model):
    """ A PEP8 run on a project """

    STATUS_CHOICES = [
        ('ok', 'ok'),
        ('err', 'err'),
        ('unknown', 'unknown'),
    ]

    project = models.ForeignKey('projects.Project', verbose_name='Project')
    time_start = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Date of run start')
    finished = models.BooleanField(verbose_name='Run finished',
                                   default=False)
    duration = models.DecimalField(default=0,
                                   max_digits=8,
                                   decimal_places=2,
                                   verbose_name='Run duration')
    status = models.CharField(verbose_name='Run status',
                              max_length=10,
                              choices=STATUS_CHOICES,
                              default='unknown')
    raw_output = models.TextField(verbose_name='Raw output')
    counters = JSONField(verbose_name='Counters')
    total_errors = models.IntegerField(verbose_name='Total errors')

    bsct_list_fields = [project, time_start, total_errors]

    def __unicode__(self):
        return "Run for {} at {}".format(self.project.name, self.time_start)

    def duration_detail(self):
        return "{} s".format(self.duration)

    def finished_detail(self):
        return "Finished" if self.finished else "Still running..."

    def _get_message_counters(self):
        from models import PEP8Message
        return [
            {
                'message': PEP8Message.objects.get(code=counter),
                'count': self.counters[counter],
            }
            for counter in self.counters if counter[0:1] in ('E', 'W',)
        ]
    message_counters = property(_get_message_counters)

    class Meta:
        verbose_name = "PEP8 run"
        verbose_name_plural = "PEP8 runs"


class PEP8Message(BSCTModelMixin, models.Model):
    """ A PEP8 error/warning """
    code = models.CharField(verbose_name='Code', max_length=4, primary_key=True)
    message = models.TextField(verbose_name='Message')

    types = {'W': 'warning', 'E': 'error'}

    def __unicode__(self):
        return "{} : {}".format(self.code, self.message)

    def _get_type(self):
        return self.types[self.code[0:1]]
    type = property(_get_type)

    class Meta:
        verbose_name = "PEP8 error / warning"
        verbose_name_plural = "PEP8 errors / warnings"
