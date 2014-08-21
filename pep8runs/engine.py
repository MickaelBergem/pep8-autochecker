""" Engine of PEP8 runner """

import pep8
from projects.models import Project
from pep8runs.models import Run


class PEP8Runner:
    """ PEP8 checks runner """

    def __init__(self):
        self.pep8style = pep8.StyleGuide(quiet=True)

    def run(self, project):
        result = self.pep8style.check_files(['manage.py', 'pep8runs/models.py'])
        return result

    def run_and_save(self, project):
        res = self.run(project)
        # TODO : save...
