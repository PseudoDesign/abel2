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


def planet_info(planet_id):
    return client.execute_op('get_universe_planets_planet_id', planet_id=planet_id).data


def stargate_info(stargate_id):
    return client.execute_op('get_universe_stargates_stargate_id', stargate_id=stargate_id).data


def station_info(station_id):
    return client.execute_op('get_universe_stations_station_id', station_id=station_id).data


def structure_orders(structure_id):
    return client.execute_op('get_markets_structures_structure_id', structure_id=structure_id).data
