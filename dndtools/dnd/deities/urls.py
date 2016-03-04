from django.conf.urls import patterns, url
from .views import  deity_list, deity_detail


app_name = 'deities'
urlpatterns = [
    # deities
    url(r'^$', deity_list, name='deity_list'),

    # deities > detail
    url(r'^(?P<deity_slug>[^/]+)/$', deity_detail, name='deity_detail')
]
