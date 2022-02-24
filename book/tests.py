from django.test import TestCase
from book.models import Author

class AuthorTestCase(TestCase):
    def setUp(self):
        Author.objects.create(first_name="Brian", last_name="Tracy")

    def test_author_creation(self):
        """Author creation test"""
        first_name = Author.objects.get(first_name="Brian").first_name
        last_name = Author.objects.get(first_name="Brian").last_name

        self.assertEqual(first_name, 'Brian')
        self.assertEqual(last_name, "Tracy")
