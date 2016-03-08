from django.conf.urls import patterns, url
from .views import rulebook_list_mobile, edition_list_mobile, edition_detail_mobile, rulebook_detail_mobile


app_name = 'rulebooks'
urlpatterns = [
    # rulebooks
    url(
        r'^$', rulebook_list_mobile,
        name='rulebook_list_mobile',
    ),
    # rulebooks > editions
    url(
        r'^editions/$', edition_list_mobile,
        name='edition_list_mobile',
    ),
    # rulebooks > edition (lists books in an edition)
    url(
        r'^(?P<edition_slug>[^/]+)--(?P<edition_id>\d+)/$', edition_detail_mobile,
        name='edition_detail_mobile',
    ),
    # rulebooks > edition > rulebook (rulebook detail, links to spells/feats)
    url(
        r'^(?P<edition_slug>[^/]+)--(?P<edition_id>\d+)/(?P<rulebook_slug>[^/]+)--(?P<rulebook_id>\d+)/$', rulebook_detail_mobile,
        name='rulebook_detail_mobile',
    ),
]
