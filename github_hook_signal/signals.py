from django.dispatch import Signal


# A Github hook has been received
github_hook_received = Signal(providing_args=["repository", "payload"])
