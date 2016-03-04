from django.conf.urls import patterns, url
from . import views

app_name = 'rulebooks'
urlpatterns = [
    # rulebooks
    url(r'^$', views.rulebook_list, name='rulebook_list'),

    # rulebooks > editions
    url(r'^editions/$', views.edition_list, name='edition_list'),

    # rulebooks > edition (lists books in an edition)
    url(r'^(?P<edition_slug>[^/]+)--(?P<edition_id>\d+)/$',
        views.edition_detail, name='edition_detail'),

    # rulebooks > edition > rulebook (rulebook detail, links to spells/feats)
    url(r'^(?P<edition_slug>[^/]+)--(?P<edition_id>\d+)/(?P<rulebook_slug>[^/]+)--(?P<rulebook_id>\d+)/$',
        views.rulebook_detail, name='rulebook_detail'),
]

