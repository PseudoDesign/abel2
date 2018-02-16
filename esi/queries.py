from .client import Client

client = Client()


def items():
    pass


def item_groups():
    return client.execute_op('get_markets_groups').data


def item_group_info(group_id):
    return client.execute_op('get_markets_groups_market_group_id', market_group_id=group_id)
