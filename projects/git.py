""" GIT support """

import subprocess
import os
import logging
from pep8autochecker import settings


class GitProject:
    """ A GIT repository """

    def __init__(self, project):
        self.project = project
        try:
            os.mkdir(settings.PATH_CLONE_PROJECTS)
        except OSError:
            pass  # Temp rootdir already exists

    def git_get(self):
        # We assume the remote URL has not changed
        if os.path.isdir(self.get_clone_dir()):
            f = self.git_pull()
        else:
            f = self.git_clone()
        return f == 0

    def git_clone(self):
        logging.info("Clone project #%d (%s) : %s"
                     % (self.project.id, self.project.name, self.project.git_url_clone))
        cmd = ['git',
               'clone',
               self.project.git_url_clone,
               self.get_clone_dir()]
        p = subprocess.Popen(cmd, cwd=settings.PATH_CLONE_PROJECTS)
        p.wait()

        return p.returncode

    def git_pull(self):
        logging.info("Pull project #%d (%s) : %s"
                     % (self.project.id, self.project.name, self.project.git_url_clone))
        cmd = ['git', 'pull']
        p = subprocess.Popen(cmd, cwd=self.get_clone_dir())
        p.wait()

        return p.returncode

    def get_clone_dir(self):
        return os.path.join(settings.PATH_CLONE_PROJECTS,
                            'git-%d' % self.project.id)
