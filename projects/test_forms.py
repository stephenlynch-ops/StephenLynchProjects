import unittest
from django.test import TestCase
from .forms import ProjectForm


class TestProjectForm(TestCase):
    """ Inherits TestCase for all tests below """
    def test_project_title_is_required(self):
        """ Tests to see if the project title is a required field """
        form = ProjectForm({'project_title': ''})
        self.assertFalse(form.is_valid())
