from django.test import TestCase

from engine import PEP8Runner
from projects.models import Project
from pep8runs.models import Run


class EngineTests(TestCase):

    def setUp(self):
        self.project1 = Project.objects.create(
            name="UpTimeDelay",
            git_url_clone="https://github.com/MickaelBergem/UpTimeDelay.git"
        )

    def test_can_run(self):
        """ Can it run ? """
        self.assertEqual(Run.objects.count(), 0)

        engine = PEP8Runner()
        run = engine.run(self.project1)

        self.assertIsInstance(run, Run)
        self.assertEqual(Run.objects.count(), 0,
                         msg="The run method should not save the run")

    def test_can_run_and_save(self):
        """ Can it save the run ? """
        engine = PEP8Runner()

        self.assertEqual(Run.objects.count(), 0)

        run_retour = engine.run_and_save(self.project1)

        self.assertEqual(Run.objects.count(), 1,
                         msg="The run_and_save method should save the run")

        run = Run.objects.first()
        self.assertEqual(run_retour, run)

        self.assertEqual(run.finished, True)
