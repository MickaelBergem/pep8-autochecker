from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.views.generic import ListView, CreateView
from views import RunsList, ProjectDetail

from bsct.urls import URLGenerator

from models import Project
bsct_patterns_project = URLGenerator(Project).get_urlpatterns(paginate_by=10)

urlpatterns = patterns(
    '',
    url('^project/$',
        ListView.as_view(model=Project, template_name="projects/project_list.html"),
        name='project_list'),

    url('^project/(?P<pk>\d+)$',
        ProjectDetail.as_view(),
        name='project_detail'),

    url('^project/new/?$',
        CreateView.as_view(model=Project, template_name="projects/project_create.html"),
        name='project_create'),

    url('^project/(?P<pk>\d+)/runs$',
        RunsList.as_view(),
        name='project_runs_list'),

    url('', include(bsct_patterns_project)),
)
