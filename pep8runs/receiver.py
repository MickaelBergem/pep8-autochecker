from django.dispatch import receiver
from github_hook_signal.signals import github_hook_received
import logging

from engine import PEP8Runner
from projects.models import Project


@receiver(github_hook_received)
def trigger_run(sender, **kwargs):
    logging.debug("Received a github hook for repository '%s'"
                  % kwargs['repository'])

    try:
        project = Project.objects.get(git_url_clone=kwargs['repository']['url'])
    except Project.DoesNotExist:
        return {'status': 'failed', 'message': "No such repository !"}

    engine = PEP8Runner()

    run = engine.run_and_save(project)

    return {'status': 'success', 'message': "Run succeed"}
