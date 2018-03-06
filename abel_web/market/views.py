from django.shortcuts import render
from django.urls import reverse
import esi


# Create your views here.
def items(request):
    """
    Returns a list of all of the available types of items.  Uses the "basic_table" template.
    :param request:
    :return:
    """
    item_groups = esi.queries.item_groups()
    item_group_info = [esi.queries.item_group_info(item_id) for item_id in item_groups]
    context = {
        'table_entries': item_group_info
    }
    return render(request, 'market/basic_list.html', context)


def regions(request):
    """
    Generates a basic table with descriptions of all regions.  url points to that region's page
    :param request:
    :return:
    """
    region_ids = esi.queries.regions()
    table_entries = []
    for region_id in region_ids:
        table_entries.append({
            'id': region_id,
            'info': esi.queries.region_info(region_id)['name'],
            'url': reverse("market:region", kwargs={'region_id': region_id})
        })
    context = {
        'table_entries': table_entries,
    }
    return render(request, 'market/basic_list.html', context)


def region(request, region_id):
    """
    Displays information about the region using the "basic.html" template
    :param request:
    :param region_id:
    :return:
    """
    region_info = esi.queries.region_info(region_id)
    constellations = []
    for constellation_id in region_info['constellations']:
        constellations.append({
            'id': constellation_id,
            'info': esi.queries.constellation_info(constellation_id)['name'],
            'url': reverse("market:constellation", kwargs={'constellation_id': constellation_id})
        })

    entries = [
        {
            'type': 'id',
            'value': region_id
        },
        {
            'type': 'text',
            'title': 'Description',
            'value': region_info['description']
        },
        {
            'type': 'list',
            'title': 'Constellations',
            'value': constellations
        }
    ]
    context = {
        'entries': entries,
        'title': region_info['name']
    }
    return render(request, 'market/basic.html', context)


def constellation(request, constellation_id):
    """
    Displays information about the constellation using the "basic.html" template
    :param request:
    :param constellation_id:
    :return:
    """
    constellation_info = esi.queries.constellation_info(constellation_id)
    region_id = constellation_info['region_id']
    region_name = esi.queries.region_info(region_id)['name']
    systems = []
    for system_id in constellation_info['systems']:
        systems.append({
            'id': system_id,
            'info': esi.queries.system_info(system_id)['name'],
            'url': reverse("market:system", kwargs={'system_id': system_id})
        })
    entries = [
        {
            'type': 'id',
            'value': constellation_id
        },
        {
            'type': 'text',
            'title': 'Region',
            'value': region_name,
            'url': reverse("market:region", kwargs={'region_id': region_id})
        },
        {
            'type': 'coord',
            'title': 'Position',
            'value': {
                'x': constellation_info['position']['x'],
                'y': constellation_info['position']['y'],
                'z': constellation_info['position']['z']
            }
        },
        {
            'type': 'list',
            'title': "Systems",
            'value': systems
        }
    ]
    context = {
        'title': constellation_info['name'],
        'entries': entries
    }
    return render(request, 'market/basic.html', context)


def system(request, system_id):
    """
    Displays information about the system using the "basic.html" template
    :param request:
    :param system_id:
    :return:
    """
    system_info = esi.queries.system_info(system_id)
    constellation_id = system_info['constellation_id']
    constellation_info = esi.queries.constellation_info(constellation_id)
    planets = []
    stations = []
    stargates = []
    for planet_id in system_info['planets']:
        planet_id = planet_id['planet_id']
        planets.append({
            'id': planet_id,
            'info': esi.queries.planet_info(planet_id)['name']
        })
    for station_id in system_info['stations']:
        stations.append({
            'id': station_id,
            'info': esi.queries.station_info(station_id)['name'],
            'url': reverse("market:station", kwargs={'station_id': station_id})
        })
    for stargate_id in system_info['stargates']:
        destination_id = esi.queries.stargate_info(stargate_id)['destination']['system_id']
        stargates.append({
            'id': destination_id,
            'info': esi.queries.system_info(destination_id)['name'],
            'url': reverse("market:system", kwargs={'system_id': destination_id})
        })
    entries = [
        {
            'type': 'id',
            'value': system_id
        },
        {
            'type': 'text',
            'title': 'Security Status',
            'value': system_info['security_status']
        },
        {
            'type': 'text',
            'title': 'Constellation',
            'value': constellation_info['name'],
            'url': reverse("market:constellation", kwargs={'constellation_id': constellation_id})
        },
        {
            'type': 'coord',
            'title': 'Position',
            'value': {
                'x': system_info['position']['x'],
                'y': system_info['position']['y'],
                'z': system_info['position']['z']
            }
        },
        {
            'type': 'list',
            'title': "Stations",
            'value': stations
        },
        {
            'type': 'list',
            'title': "Planets",
            'value': planets
        },
        {
            'type': 'list',
            'title': "Stargates",
            'value': stargates
        }

    ]
    context = {
        'title': system_info['name'],
        'entries': entries
    }
    return render(request, 'market/basic.html', context)


def station(request, station_id):
    """
    Displays information about the station
    :param request:
    :param station_id:
    :return:
    """
    station_info = esi.queries.station_info(station_id)
    system_info = esi.queries.system_info(station_info['system_id'])
    entries = [
        {
            'type': 'id',
            'value': station_id
        },
        {
            'type': 'text',
            'title': 'System',
            'value': system_info['name'],
            'url': reverse("market:system", kwargs={'system_id': station_info['system_id']})
        },
        {
            'type': 'coord',
            'title': 'Position',
            'value': {
                'x': station_info['position']['x'],
                'y': station_info['position']['y'],
                'z': station_info['position']['z']
            }
        }
    ]
    context = {
        'title': station_info['name'],
        'entries': entries
    }
    return render(request, 'market/basic.html', context)

