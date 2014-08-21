from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView

from bsct.urls import URLGenerator

from models import Project
bsct_patterns_project = URLGenerator(Project).get_urlpatterns(paginate_by=10)

urlpatterns = patterns('',
                       url('', include(bsct_patterns_project)),
                       )
