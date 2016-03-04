from django.conf.urls import patterns, url
from .views import item_index, item_list_by_rulebook, items_in_rulebook, item_detail


app_name = 'items'
urlpatterns = [
    # items
    url(r'^$', item_index, name='item_index'),

    # items > by rulebooks
    url(r'^by-rulebooks/$', item_list_by_rulebook, name='item_list_by_rulebook'),

    # items > rulebook
    url(r'^(?P<rulebook_slug>[^/]+)--(?P<rulebook_id>\d+)/$', items_in_rulebook, name='items_in_rulebook'),

    # items > rulebook > item
    url(r'^(?P<rulebook_slug>[^/]+)--(?P<rulebook_id>\d+)/(?P<item_slug>[^/]+)--(?P<item_id>\d+)/$',
        item_detail, name='item_detail')
]
