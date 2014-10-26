from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from models import Project
from pep8runs.models import Run


class RunsList(ListView):
    context_object_name = "liste_bdc"
    template_name = "bsct/plain/list.html"

    def get_queryset(self):
        self.project = get_object_or_404(Project, id=self.kwargs['pk'])
        return Run.objects.filter(project=self.project)
