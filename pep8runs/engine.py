""" Engine of PEP8 runner """

import pep8
import logging
import simplejson
from pep8runs.models import Run, PEP8Message
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

        self.pep8style.input_dir(git_repo.get_clone_dir())
        result = self.pep8style.check_files()

        run.status = 'ok'
        run.finished = True
        run.duration = result.elapsed
        # run.raw_output = result.messages
        run.total_errors = result.total_errors
        run.counters = result.counters

        # Adding messages if they have never been seen before
        for message_code in result.messages:
            PEP8Message.objects.update_or_create(
                code=message_code,
                message=result.messages[message_code]
            )

        logging.info("Run for project #%d finished after %ds with %d error(s)."
                     % (project.id, run.duration, run.total_errors))

        return run

    def run_and_save(self, project):
        run = self.run(project)
        run.save()

        return run
