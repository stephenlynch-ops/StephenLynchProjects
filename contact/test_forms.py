import unittest
from django.test import TestCase
from .forms import ContactForm


class TestProjectForm(TestCase):
    """ Inherits TestCase for all tests below """
    def test_contact_form_create_ok(self):
        """ Test to see if we can create a test contact form """
        form = ContactForm({'email':'me@world.com'})
        self.assertTrue(form.is_valid())
