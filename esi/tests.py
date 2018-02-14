from unittest import TestCase
from unittest.mock import MagicMock, patch
from esi.client import Client
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


class TestQueries(TestCase):
    def test_get_items(self):
        pass

    @patch("esi.queries.client")
    def test_get_item_groups(self, client):
        client.execute_op.return_value = "item_groups"
        return_value = esi.queries.item_groups()
        client.execute_op.assert_called_with('get_markets_groups')
        self.assertEqual(return_value, "item_groups")


