from django.apps import AppConfig


class PEP8RunsConfig(AppConfig):

    name = 'pep8runs'
    verbose_name = 'PEP8 Checks'

    def ready(self):
        # import signal handlers
        import pep8runs.receiver
