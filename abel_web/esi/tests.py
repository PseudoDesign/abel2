from unittest import TestCase
from unittest.mock import MagicMock, patch
from .client import Client
import esi


class TestClient(TestCase):

    def test_disconnected_on_startup(self):
        client = Client()
        self.assertFalse(client.is_connected)

    def test_connect_opens_connection(self):
        client = Client()
        client._open = MagicMock()
        client.connect()
        client._open.assert_called_once()
        self.assertTrue(client.is_connected)

    def test_calling_connect_when_already_connected_does_nothing(self):
        client = Client()
        client.is_connected = True
        client._open = MagicMock()
        client.connect()
        client._open.assert_not_called()

    def test_execute_op(self):
        op = "op"
        op_args = {
            '1': 1,
            '2': 2,
        }
        client = Client()
        client.is_connected = True
        client.esi_app = MagicMock()
        client.esi_app.op[op].return_value = "internal_op"
        client.esi_client = MagicMock()
        client.esi_client.request.return_value = "return"
        return_value = client.execute_op(op, **op_args)
        self.assertEqual(return_value, "return")
        client.esi_app.op[op].assert_called_with(**op_args)
        client.esi_client.request.assert_called_with("internal_op")

    def test__open(self):
        pass


class TestQueries(TestCase):
    def test_get_items(self):
        pass

    @patch("esi.queries.client")
    def test_get_item_groups(self, client):
        client.execute_op.return_value.data = "item_groups"
        return_value = esi.queries.item_groups()
        client.execute_op.assert_called_with('get_markets_groups')
        self.assertEqual(return_value, "item_groups")

    @patch("esi.queries.client")
    def test_get_item_group_info(self, client):
        client.execute_op.return_value.data = "group_info"
        return_value = esi.queries.item_group_info(13)
        client.execute_op.assert_called_with('get_markets_groups_market_group_id', market_group_id=13)
        self.assertEqual(return_value, "group_info")

    @patch("esi.queries.client")
    def test_get_regions(self, client):
        client.execute_op.return_value.data = "regions"
        return_value = esi.queries.regions()
        client.execute_op.assert_called_with('get_universe_regions')
        self.assertEqual(return_value, "regions")

    @patch("esi.queries.client")
    def test_get_region_info(self, client):
        client.execute_op.return_value.data = "region_info"
        return_value = esi.queries.region_info(13)
        client.execute_op.assert_called_with('get_universe_regions_region_id', region_id=13)
        self.assertEqual(return_value, "region_info")

    @patch("esi.queries.client")
    def test_get_constellations(self, client):
        client.execute_op.return_value.data = "constellations"
        return_value = esi.queries.constellations()
        client.execute_op.assert_called_with('get_universe_constellations')
        self.assertEqual(return_value, "constellations")

    @patch("esi.queries.client")
    def test_get_constellation_info(self, client):
        client.execute_op.return_value.data = "constellation_info"
        return_value = esi.queries.constellation_info(13)
        client.execute_op.assert_called_with('get_universe_constellations_constellation_id', constellation_id=13)
        self.assertEqual(return_value, "constellation_info")

    @patch("esi.queries.client")
    def test_get_systems(self, client):
        client.execute_op.return_value.data = "systems"
        return_value = esi.queries.systems()
        client.execute_op.assert_called_with('get_universe_systems')
        self.assertEqual(return_value, "systems")

    @patch("esi.queries.client")
    def test_get_system_info(self, client):
        client.execute_op.return_value.data = "system_info"
        return_value = esi.queries.system_info(13)
        client.execute_op.assert_called_with('get_universe_systems_system_id', system_id=13)
        self.assertEqual(return_value, "system_info")
