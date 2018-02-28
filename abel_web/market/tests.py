from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch, MagicMock


class TestRegionsView(TestCase):
    @patch("esi.queries.regions")
    @patch("esi.queries.region_info")
    def setUp(self, region_info, regions):
        self.region_info = MagicMock()
        region_info.return_value = self.region_info
        regions.return_value = [1, 2]
        self.client = Client()
        self.response = self.client.get(reverse('market:regions'))

    def test_response_returns_table_entry_of_regions(self):
        self.assertEqual(
            self.response.context['table_entries'],
            [
                {
                    'id': 1,
                    'info': self.region_info['name'],
                    'url': reverse("market:region", kwargs={'region_id': 1}),
                },
                {
                    'id': 2,
                    'info': self.region_info['name'],
                    'url': reverse("market:region", kwargs={'region_id': 2}),
                }
            ]
        )

    def test_response_returns_status_200(self):
        self.assertEqual(self.response.status_code, 200)


class TestRegionView(TestCase):
    @patch("esi.queries.region_info")
    @patch("esi.queries.constellation_info")
    def setUp(self, constellation_info, region_info):
        self.region_info = MagicMock()
        self.constellation_info = MagicMock()
        constellation_info.return_value = self.constellation_info
        region_info.return_value = self.region_info
        self.client = Client()
        self.response = reverse("market:region", kwargs={'region_id': 1})