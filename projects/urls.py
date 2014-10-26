from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.views.generic import ListView

from bsct.urls import URLGenerator

from projects.views import ProjectDetailView

from models import Project
bsct_patterns_project = URLGenerator(Project).get_urlpatterns(paginate_by=10)

urlpatterns = patterns('',
                       url('^project/$',
                           ListView.as_view(model=Project, template_name="projects/project_list.html"),
                           name='project_list'),
                       url('^project/(?P<pk>\d+)$', ProjectDetailView.as_view(), name='project_detail'),
                       url('', include(bsct_patterns_project)),
                       )
