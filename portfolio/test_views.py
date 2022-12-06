from django.test import TestCase


class TestViews(TestCase):
    """ Inherits TestCase for all functions below
    """
    def test_open_home_page_works(self):
        """ Test the corrrect template is used
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')