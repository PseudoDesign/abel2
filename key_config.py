import yaml


def load(filename, required_keys):
    """
    Loads the provided yaml file and makes sure it contains the top-level keys listed in required_keys.
    :param filename:
    :param required_keys: A list of dictionaries.  Example:
        [
            {'name': 'the_key_name', 'description': 'A description of this key'},
        ]
    :return:
    """
    with open(filename, 'r') as stream:
        try:
            keys = yaml.load(stream)
        except yaml.YAMLError:
            raise IOError("Unable to open key/config file: {0}".format(filename))
    for k in required_keys:
        if keys is None or k['name'] not in keys:
            raise ValueError("Required key {0} was not found in {1}".format(k['name'], filename))
    return keys
