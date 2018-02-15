from unittest import TestCase
from unittest.mock import patch, mock_open
import key_config


class TestKeyConfig(TestCase):
    @patch('yaml.load')
    @patch("builtins.open", new_callable=mock_open, read_data="yaml_data")
    def test_load_config_loads_yaml_file(self, mock_file, yaml_load):
        required_keys = [
            {
                'name': "sample_key",
                'description': "sample_description"
            }
        ]
        yaml_load.return_value = {'sample_key': "sample_value"}
        return_value = key_config.load("key_file", required_keys)
        self.assertEqual(yaml_load.return_value, return_value)

    def test_load_config_file_not_found_raises_io_error(self):
        with self.assertRaises(IOError):
            key_config.load("a file that doesn't exist$$", None)

    @patch('yaml.load')
    @patch("builtins.open", new_callable=mock_open, read_data="yaml_data")
    def test_load_config_missing_required_keys_raises_value_error(self, mock_file, yaml_load):
        required_keys = [
            {
                'name': "sample_key",
                'description': "sample_description"
            }
        ]
        yaml_load.return_value = {'not_sample_key': "sample_value"}
        with self.assertRaises(ValueError):
            key_config.load("key_file", required_keys)

