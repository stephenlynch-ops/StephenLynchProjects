from django.test import TestCase
from .models import Project


class TestProjectModel(TestCase):
    """ Inherits TestCase for all functions below
    """

    def test_project_creation(self):
        """ Tests to see if a project can be created as expected """
        project = Project.objects.create(project_title="Some Project")
        self.assertEqual(project.project_title, "Some Project")
