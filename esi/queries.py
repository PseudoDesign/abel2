from .client import Client

client = Client()


def items():
    pass


def item_groups():
    return client.execute_op('get_markets_groups')
