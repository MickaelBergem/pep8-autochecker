from django.apps import AppConfig


class GithubHookSignalConfig(AppConfig):

    name = 'github_hook_signal'
    verbose_name = 'Signals incoming Github hooks'

    def ready(self):
        # import signal handlers
        import github_hook_signal.signals
