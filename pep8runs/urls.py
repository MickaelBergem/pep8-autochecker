from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView

from bsct.urls import URLGenerator

from pep8runs.views import RunDetailView

from models import Run
bsct_patterns_run = URLGenerator(Run).get_urlpatterns(paginate_by=10)

urlpatterns = patterns('',
                       url(r'^manual_run/(?P<project_id>[0-9]+)$', 'pep8runs.views.manual_run', name='manual_run'),
                       url(r'^run/(?P<pk>\d+)$',
                           RunDetailView.as_view(),
                           name='run_detail'),
                       url('', include(bsct_patterns_run)),
                       )
