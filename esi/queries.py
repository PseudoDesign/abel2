from .client import Client

client = Client()


def item_groups():
    return client.execute_op('get_markets_groups').data


def item_group_info(group_id):
    return client.execute_op('get_markets_groups_market_group_id', market_group_id=group_id).data


def regions():
    return client.execute_op('get_universe_regions').data


def region_info(region_id):
    return client.execute_op('get_universe_regions_region_id', region_id=region_id).data


def constellations():
    return client.execute_op('get_universe_constellations').data


def constellation_info(constellation_id):
    return client.execute_op('get_universe_constellations_constellation_id', constellation_id=constellation_id).data


def systems():
    return client.execute_op('get_universe_systems').data


def system_info(system_id):
    return client.execute_op('get_universe_systems_system_id', system_id=system_id).data
