from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, RedirectView
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from dnd.feeds import AdminLogFeed
from dnd.sitemap import sitemaps
from dndproject import settings
from . import views


app_name = 'dnd'
urlpatterns = [

    # index
    url(r'^$', views.index, name='index'),

    # Rulebooks
    url(r'^rulebooks/', include('dnd.rulebooks.urls')),

    # Feats
    url(r'^feats/', include('dnd.feats.urls')),

    # Spells
    url(r'^spells/', include('dnd.spells.urls')),

    # Classes
    url(r'^classes/', include('dnd.character_classes.urls')),

    # Skills
    url(r'^skills/', include('dnd.skills.urls')),

    # Races
    url(r'^races/', include('dnd.races.urls')),

    # Monsters
    url(r'^monsters/', include('dnd.monsters.urls')),

    # Items
    url(r'^items/', include('dnd.items.urls')),

    # Languages
    url(r'^languages/', include('dnd.languages.urls')),

    # Contacts
    url(r'^contacts/', include('dnd.contacts.urls')),

    # Rules
    url(r'^rules/', include('dnd.rules.urls')),

    # deities
    url(r'^deities/', include('dnd.deities.urls')),

    # OTHERS

    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),

    # inaccurate
    url(
        r'^inaccurate_content/$', views.inaccurate_content,
        name='inaccurate_content',
    ),
    # inaccurate > sent
    url(
        r'^inaccurate_content/sent/$', views.inaccurate_content_sent,
        name='inaccurate_content_sent',
    ),
    url(r'^rss.xml$', AdminLogFeed()),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}),

    # job
    url(r'^very_secret_url/$', views.very_secret_url, name='very_secret_url'),

    # MOBILE
    url(r'^m/', include('dnd.mobile.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    url('^contact/$', RedirectView.as_view(url='/contacts/')),
    url('^staff/$', RedirectView.as_view(url='/contacts/staff/')),
    url('^editions/$', RedirectView.as_view(url='/rulebooks/editions/')),
    url('^feat-(?P<feat_id>\d+)-(.*)\.html$', RedirectView.as_view(url='/feats/a--1/a--%(feat_id)s/')),
]
