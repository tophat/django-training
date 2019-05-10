from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render

NUM_OF_ITEMS = 5


def home(request, username=None):
    first_name = ''
    last_name = ''
    if username:
        user = User.objects.get(username=username)
        first_name = user.first_name
        last_name = user.last_name
        item_list = []
    else:
        item_list = []

    paginator = Paginator(item_list, NUM_OF_ITEMS)  # Show NUM_OF_ITEMS posts per page
    page = request.GET.get('page')

    items = paginator.get_page(page)

    return render(request, 'myapp/home.html', {'items': items,
                                               'first_name': first_name,
                                               'last_name': last_name})
