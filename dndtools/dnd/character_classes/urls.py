from django.conf.urls import patterns, url
from .views import character_class_list, character_class_detail, character_class_spells, character_classes_in_rulebook


app_name = 'character_classes'
urlpatterns = [
    # classes
    url(r'^$', character_class_list, name='character_class_list'),

    # classes > detail
    url(r'^(?P<character_class_slug>[^/]+)/$', character_class_detail, name='character_class_detail'),

    # classes > detail
    url(r'^(?P<rulebook_slug>[^/]+)--(?P<rulebook_id>\d+)/(?P<character_class_slug>[^/]+)/$',
        character_class_detail, name='character_class_variant_detail'),

    # classes > detail > spells by level
    url(r'^(?P<character_class_slug>[^/]+)/spells-level-(?P<level>\d)/$',
        character_class_spells, name='character_class_spells'),

    # classes > rulebook
    url(r'^rulebook/(?P<rulebook_slug>[^/]+)--(?P<rulebook_id>\d+)/$',
        character_classes_in_rulebook, name='character_classes_in_rulebook')
]
