from django.test import TestCase

from engine import PEP8Runner
from projects.models import Project
from pep8runs.models import Run


class EngineTests(TestCase):
    fixtures = ['test.json']

    def setUp(self):
        self.project1 = Project.objects.first()

    def test_can_run(self):
        """ Is the index page accessible ? """
        engine = PEP8Runner()
        engine.run(self.project1)
        # Should not raise an error
