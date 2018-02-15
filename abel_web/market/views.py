from django.shortcuts import render
import esi


# Create your views here.
def items(request):
    """
    Returns a list of all of the available types of items.  Uses the "basic_table" template.
    :param request:
    :return:
    """
    context = {
        'table_entries': esi.queries.item_groups()
    }
    return render(request, 'market/basic_table.html', context)

