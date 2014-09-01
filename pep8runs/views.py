from django.shortcuts import render, render_to_response
from pep8runs.engine import PEP8Runner
from projects.models import Project


def manual_run(request, project_id):

    project = Project.objects.get(id=project_id)

    engine = PEP8Runner()

    run = engine.run_and_save(project)

    return render_to_response('projects/manual_run.html', {'run': run})
