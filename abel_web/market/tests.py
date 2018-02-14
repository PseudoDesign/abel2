from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch


class TestItemsView(TestCase):
    @patch("esi.queries.items")
    def setUp(self, esi_items):
        esi_items.return_value = "items"
        self.client = Client()
        self.response = self.client.get(reverse('market:items'))

    def test_table_entries_response_content(self, ):
        self.assertEqual(self.response.context['table_entries'], "items")

    def test_page_returns_status_code_200(self):
        self.assertEqual(self.response.status_code, 200)
