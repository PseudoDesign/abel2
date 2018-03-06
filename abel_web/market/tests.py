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


class TestStationView(TestCase):
    @patch("esi.queries.system_info")
    @patch("esi.queries.station_info")
    def setUp(self, station_info, system_info):
        self.station_info = {
            'system_id': 11,
            'name': "Test Station",
            'position': {
                'x': 1,
                'y': 2,
                'z': -3,
            },
        }
        self.system_info = MagicMock()
        system_info.return_value = self.system_info
        station_info.return_value = self.station_info
        self.client = Client()
        self.response = self.client.get(reverse("market:station", kwargs={'station_id': 14}))

    def test_response_returns_entry_of_station_info(self):
        self.assertEqual(
            self.response.context['entries'],
            [
                {
                    'type': 'id',
                    'value': 14
                },
                {
                    'type': 'text',
                    'title': 'System',
                    'value': self.system_info['name'],
                    'url': reverse("market:system", kwargs={'system_id': 11})
                },
                {
                    'type': 'coord',
                    'title': 'Position',
                    'value': {
                        'x': 1,
                        'y': 2,
                        'z': -3
                    }
                },
            ]
        )
        self.assertEqual(
            self.response.context['title'],
            "Test Station"
        )


class TestSystemView(TestCase):
    @patch("esi.queries.station_info")
    @patch("esi.queries.stargate_info")
    @patch("esi.queries.planet_info")
    @patch("esi.queries.constellation_info")
    @patch("esi.queries.system_info")
    def setUp(self, system_info, constellation_info, planet_info, stargate_info, station_info):
        self.system_info = {
            'name': "System Name",
            'constellation_id': 42,
            'position': {
                'x': 1,
                'y': 2,
                'z': -3,
            },
            'security_status': .5,
            'stations': [1, 2, 3],
            'planets': [{'planet_id': 1}, {'planet_id': 2}],
            'stargates': [1, 2, 3, 4],
        }
        self.constellation_info = MagicMock()
        self.planet_info = MagicMock()
        self.stargate_info = {
            'destination': {
                'system_id': 42
            },
            'name': "Destination Station"
        }
        self.station_info = MagicMock()
        system_info.return_value = self.system_info
        constellation_info.return_value = self.constellation_info
        planet_info.return_value = self.planet_info
        stargate_info.return_value = self.stargate_info
        station_info.return_value = self.station_info
        self.client = Client()
        self.response = self.client.get(reverse("market:system", kwargs={'system_id': 14}))

    def test_response_returns_entry_of_system_info(self):
        self.maxDiff = None
        self.assertEqual(
            self.response.context['entries'],
            [
                {
                    'type': 'id',
                    'value': 14
                },
                {
                    'type': 'text',
                    'title': 'Security Status',
                    'value': self.system_info['security_status'],
                },
                {
                    'type': 'text',
                    'title': 'Constellation',
                    'value': self.constellation_info['name'],
                    'url': reverse("market:constellation", kwargs={'constellation_id': 42})
                },
                {
                    'type': 'coord',
                    'title': 'Position',
                    'value': {
                        'x': 1,
                        'y': 2,
                        'z': -3
                    }
                },
                {
                    'type': 'list',
                    'title': 'Stations',
                    'value': [
                        {
                            'id': 1,
                            'info': self.station_info['name'],
                            'url': reverse("market:station", kwargs={'station_id': 1}),
                        },
                        {
                            'id': 2,
                            'info': self.station_info['name'],
                            'url': reverse("market:station", kwargs={'station_id': 2}),
                        },
                        {
                            'id': 3,
                            'info': self.station_info['name'],
                            'url': reverse("market:station", kwargs={'station_id': 3}),
                        }
                    ]
                },
                {
                    'type': 'list',
                    'title': 'Planets',
                    'value': [
                        {
                            'id': 1,
                            'info': self.planet_info['name'],
                            # 'url': reverse("market:planet", kwargs={'planet_id': 1}),
                        },
                        {
                            'id': 2,
                            'info': self.planet_info['name'],
                            # 'url': reverse("market:planet", kwargs={'planet_id': 2}),
                        }
                    ]
                },
                {
                    'type': 'list',
                    'title': 'Stargates',
                    'value': [
                        {
                            'id': self.stargate_info['destination']['system_id'],
                            'info': self.system_info['name'],
                            'url': reverse("market:system", kwargs={'system_id': self.stargate_info['destination']['system_id']}),
                        },
                        {
                            'id': self.stargate_info['destination']['system_id'],
                            'info': self.system_info['name'],
                            'url': reverse("market:system", kwargs={'system_id': self.stargate_info['destination']['system_id']}),
                        },
                        {
                            'id': self.stargate_info['destination']['system_id'],
                            'info': self.system_info['name'],
                            'url': reverse("market:system", kwargs={'system_id': self.stargate_info['destination']['system_id']}),
                        },
                        {
                            'id': self.stargate_info['destination']['system_id'],
                            'info': self.system_info['name'],
                            'url': reverse("market:system", kwargs={'system_id': self.stargate_info['destination']['system_id']}),
                        }
                    ]
                }
            ]
        )
        self.assertEqual(
            self.response.context['title'],
            "System Name"
        )


class TestConstellationView(TestCase):
    @patch("esi.queries.region_info")
    @patch("esi.queries.constellation_info")
    @patch("esi.queries.system_info")
    def setUp(self, system_info, constellation_info, region_info):
        self.region_info = MagicMock()
        region_info.return_value = self.region_info
        self.constellation_info = {
            'name': "Constellation Name",
            'region_id': 1,
            'position': {
                'x': 1,
                'y': 2.2,
                'z': -1.33,
            },
            'systems': [3, 5]
        }
        self.system_info = MagicMock()
        system_info.return_value = self.system_info
        constellation_info.return_value = self.constellation_info
        self.client = Client()
        self.response = self.client.get(reverse("market:constellation", kwargs={'constellation_id': 13}))

    def test_response_returns_entry_of_constellation_info(self):
        self.maxDiff = None
        self.assertEqual(
            self.response.context['entries'],
            [
                {
                    'type': 'id',
                    'value': 13
                },
                {
                    'type': 'text',
                    'title': 'Region',
                    'value': self.region_info['name'],
                    'url': reverse("market:region", kwargs={'region_id': 1})
                },
                {
                    'type': 'coord',
                    'title': 'Position',
                    'value': {
                        'x': 1,
                        'y': 2.2,
                        'z': -1.33
                    }
                },
                {
                    'type': 'list',
                    'title': 'Systems',
                    'value': [
                        {
                            'id': 3,
                            'info': self.system_info['name'],
                            'url': reverse("market:system", kwargs={'system_id': 3}),
                        },
                        {
                            'id': 5,
                            'info': self.system_info['name'],
                            'url': reverse("market:system", kwargs={'system_id': 5}),
                        }
                    ]
                }
            ]
        )
        self.assertEqual(
            self.response.context['title'],
            "Constellation Name"
        )


class TestRegionView(TestCase):
    @patch("esi.queries.region_info")
    @patch("esi.queries.constellation_info")
    def setUp(self, constellation_info, region_info):
        self.region_info = {
            'name': "Region Name",
            'description': "a whole bunch of text",
            'constellations': [1, 2]
        }
        self.constellation_info = MagicMock()
        constellation_info.return_value = self.constellation_info
        region_info.return_value = self.region_info
        self.client = Client()
        self.response = self.client.get(reverse("market:region", kwargs={'region_id': 1}))

    def test_response_returns_entry_of_region_info(self):
        self.maxDiff = None
        self.assertEqual(
            self.response.context['entries'],
            [
                {
                    'type': 'id',
                    'value': 1
                },
                {
                    'type': 'text',
                    'title': 'Description',
                    'value': self.region_info['description']
                },
                {
                    'type': 'list',
                    'title': 'Constellations',
                    'value': [
                        {
                            'id': 1,
                            'info': self.constellation_info['name'],
                            'url': reverse("market:constellation", kwargs={'constellation_id': 1}),
                        },
                        {
                            'id': 2,
                            'info': self.constellation_info['name'],
                            'url': reverse("market:constellation", kwargs={'constellation_id': 2}),
                        }
                    ]
                }
            ]
        )
        self.assertEqual(
            self.response.context['title'],
            "Region Name"
        )

    def test_response_returns_status_200(self):
        self.assertEqual(self.response.status_code, 200)

