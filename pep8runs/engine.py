""" Engine of PEP8 runner """

import pep8
from projects.models import Project
from pep8runs.models import Run


class PEP8Runner:
    """ PEP8 checks runner """

    def __init__(self):
        self.pep8style = pep8.StyleGuide(quiet=True)

    def run(self, project):

        run = Run(project=project, finished=False)

        result = self.pep8style.check_files(['manage.py', 'pep8runs/models.py'])

        run.status = 'ok'
        run.finished = True
        run.duration = result.elapsed
        run.raw_output = result.messages

        return run

    def run_and_save(self, project):
        run = self.run(project)
        run.save()

        return run
