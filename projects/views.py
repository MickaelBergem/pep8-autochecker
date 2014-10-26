from django.shortcuts import render
from django.views.generic import DetailView

from projects.models import Project
from django_treeviewer.views import TreeViewer
from projects.git import GitProject


class ProjectDetailView(DetailView):
    model = Project
    template_name = "projects/project_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)

        git_repo = GitProject(context['object'])
        tree_viewer = TreeViewer(git_repo.get_clone_dir())

        context['tree_as_dict'] = tree_viewer.render_to_dict()
        return context
