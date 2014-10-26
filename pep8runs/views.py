from django.shortcuts import redirect
from pep8runs.engine import PEP8Runner
from projects.models import Project
from django.core.urlresolvers import reverse
from django.views.generic import DetailView

from models import Run


def manual_run(request, project_id):

    project = Project.objects.get(id=project_id)

    engine = PEP8Runner()

    run = engine.run_and_save(project)

    return redirect(run)


class RunDetailView(DetailView):
    model = Run
    template_name = "runs/run_detail.html"


