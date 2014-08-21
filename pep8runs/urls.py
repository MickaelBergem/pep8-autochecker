from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView

from bsct.urls import URLGenerator

from models import Run
bsct_patterns_run = URLGenerator(Run).get_urlpatterns(paginate_by=10)

urlpatterns = patterns('',
                       url('', include(bsct_patterns_run)),
                       )
