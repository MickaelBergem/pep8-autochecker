from django.conf.urls import url, patterns
from views import github_hook


urlpatterns = patterns('', url(r'^$', github_hook, name='github_hook'))
