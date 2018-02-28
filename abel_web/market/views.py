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
    return render(request, 'market/basic_table.html', context)


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
    return render(request, 'market/basic_table.html', context)


def region(request, region_id):
    """

    :param request:
    :param region_id:
    :return:
    """
    pass