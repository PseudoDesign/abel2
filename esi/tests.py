from unittest import TestCase
from unittest.mock import MagicMock
from esi.client import Client


class TestClient(TestCase):

    def test_disconnected_on_startup(self):
        client = Client()
        self.assertFalse(client.is_connected())

    def test_connect_opens_connection(self):
        client = Client()
        client._open = MagicMock()
        client.connect()
        client._open.assert_called_once()

    def test_calling_connect_when_already_connected_does_nothing(self):
        client = Client()
        client.is_connected = MagicMock(return_value=True)
        client._open = MagicMock()
        client.connect()
        client._open.assert_not_called()


class TestQueries(TestCase):
    def test_get_items(self):
        pass

