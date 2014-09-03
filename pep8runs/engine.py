""" Engine of PEP8 runner """

import pep8
import logging
import os
from pep8runs.models import Run
from projects.git import GitProject


class PEP8Runner:
    """ PEP8 checks runner """

    def __init__(self):
        self.pep8style = pep8.StyleGuide()

    def run(self, project):

        run = Run(project=project, finished=False)

        git_repo = GitProject(project)

        if not git_repo.git_get():
            # Clone failed
            run.status = 'err'
            run.finished = True
            run.total_errors = 0
            return run

        list_python_files = git_repo.find_files('py')
        logging.info("Found %d file(s) in repo." % len(list_python_files))
        logging.info(list_python_files)

        result = self.pep8style.check_files(list_python_files)

        run.status = 'ok'
        run.finished = True
        run.duration = result.elapsed
        run.raw_output = result.messages
        run.total_errors = result.total_errors
        run.counters = result.counters

        return run

    def run_and_save(self, project):
        run = self.run(project)
        run.save()

        return run
