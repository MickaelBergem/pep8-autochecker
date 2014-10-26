from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from models import Project
from pep8runs.models import Run


class RunsList(ListView):
    context_object_name = "liste_bdc"
    template_name = "bsct/plain/list.html"

    def get_queryset(self):
        self.project = get_object_or_404(Project, id=self.kwargs['pk'])
        return Run.objects.filter(project=self.project)


class ProjectDetail(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'

    def get_plot(self):
        plot = {'title': 'Number of issues'}

        plot_list = []

        total_errors_list = [
            [run.time_start.ctime(), run.total_errors]
            for run in Run.objects.filter(project=self.object).order_by('time_start').all()
        ]

        plot_list.append({'points': total_errors_list, 'label': 'Number of total issues'})

        plot['plot_list'] = plot_list

        return plot
