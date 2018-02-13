from django.test import TestCase, Client
from django.urls import reverse


# Create your tests here.
class TestItemsView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_item_list(self):
        response = self.client.get(reverse('market:items'))
