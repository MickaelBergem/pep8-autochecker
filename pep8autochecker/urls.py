from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$',
                           TemplateView.as_view(template_name='home.html'),
                           name='home'),
                       url(r'', include('pep8runs.urls')),
                       url(r'', include('projects.urls')),
                       url(r'githubhook', include('github_hook_signal.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       )
