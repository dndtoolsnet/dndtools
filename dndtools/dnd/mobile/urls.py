from django.conf.urls import patterns, url, include
from .views import force_desktop_version, return_to_mobile_version


app_name = 'mobile'
urlpatterns = [
    # force desktop
    url(r'^force-desktop-version/$', force_desktop_version, name='force_desktop_version'),

    # return to mobile version
    url(r'^return-to-mobile-version/$', return_to_mobile_version, name='return_to_mobile_version'),

    # index
    url(r'^', include('dnd.mobile.index.urls')),

    # character classes
    url(r'^classes/', include('dnd.mobile.character_classes.urls')),

    # feats
    url(r'^feats/', include('dnd.mobile.feats.urls')),

    # items
    url(r'^items/', include('dnd.mobile.items.urls')),

    # languages
    url(r'^languages/', include('dnd.mobile.languages.urls')),

    # monsters
    url(r'^monsters/', include('dnd.mobile.monsters.urls')),

    # races
    url(r'^races/', include('dnd.mobile.races.urls')),

    # rulebooks
    url(r'^rulebooks/', include('dnd.mobile.rulebooks.urls')),

    # rules
    url(r'^rules/', include('dnd.mobile.rules.urls')),

    # skills
    url(r'^skills/', include('dnd.mobile.skills.urls')),

    # spells
    url(r'^spells/', include('dnd.mobile.spells.urls')),

    # deities
    url(r'^deities/', include('dnd.mobile.deities.urls')),
]
