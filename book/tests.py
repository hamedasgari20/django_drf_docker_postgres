from django.test import TestCase
from book.models import Author

class AuthorTestCase(TestCase):
    def setUp(self):
        Author.objects.create(first_name="Brian", last_name="Tracy")
        Author.objects.create(first_name="Antony", last_name="Rabins")


    def test_author_creation(self):
        """Author creation test"""
        brian_tracy = Author.objects.get(first_name="Brian", last_name="Tracy")
        antony_rabins = Author.objects.get(first_name="Antony", last_name="Rabins")
        self.assertEqual(brian_tracy, 'Brian Tracy')
        self.assertEqual(antony_rabins, 'Antony Rabins')
