from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch


class TestRegionView(TestCase):
    @patch("esi.queries.regions")
    @patch("esi.queries.region_info")
    @patch("esi.queries.constellation_info")
    def setUp(self, constellation_info, region_info, regions):
        constellation_info.return_value = "constellation_info"
        region_info.return_value = "region_info"
        regions.return_value = ["region_id_1", "region_id_2"]
        self.client = Client()

    def test_root_response_returns_table_entry_of_regions(self):
        self.response = self.client.get(reverse('market:regions'))
        self.assertEqual(
            self.response.context['table_entries'],
            [
                {
                    'id': "region_id_1",
                    'info': "region_info",
                    'url': reverse("region", kwargs={'id': 'region_id_1'}),
                },
                {
                    'id': "region_id_2",
                    'info': "region_info",
                    'url': reverse("region", kwargs={'id': 'region_id_2'}),
                }
            ]
        )
