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
    pass
