from django.shortcuts import render
import esi


# Create your views here.
def items(request):
    """
    Returns a list of all of the available types of items.  Uses the "basic_table" template.
    :param request:
    :return:
    """
    item_groups = esi.queries.item_groups()
    item_group_info = [esi.queries.item_group_info(item_id).data for item_id in item_groups]
    context = {
        'table_entries': item_group_info
    }
    return render(request, 'market/basic_table.html', context)

