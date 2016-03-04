from django.shortcuts import render
from dnd.menu import menu_item
from dnd.models import NewsEntry


@menu_item("home")
def index_mobile(request):
    news_entries = NewsEntry.objects.filter(enabled=True).order_by('-published')[:15]

    response = render(request, 'dnd/mobile/index/index.html',  context={'newsEntries': news_entries,},)

    if len(news_entries):
        response.set_cookie('top_news', news_entries[0].pk, 10 * 365 * 24 * 60 * 60)

    return response
