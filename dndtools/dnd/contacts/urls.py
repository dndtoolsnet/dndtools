from django.conf.urls import patterns, url
from .views import contact, contact_sent, staff


app_name = 'contacts'
urlpatterns = [
    # contact
    url(r'^$', contact, name='contact'),

    # contact > sent
    url(r'^sent/$', contact_sent, name='contact_sent'),

    # staff
    url(r'^staff/$', staff, name='staff'),
]
