from django.test import TestCase
from django.core.urlresolvers import reverse


# Visibility of pages
class GlobalTests(TestCase):
    def test_index_accessible(self):
        """ Is the index page accessible ? """
        response = self.client.get(reverse('home'), follow=True)
        self.assertEqual(response.status_code, 200,
                         "The homepage should have a HTTP 200 response code.")
