from django.conf.urls import patterns, url
from .views import deity_list_mobile, deity_detail_mobile


app_name = 'deities'
urlpatterns = [
    # deities
    url(
        r'^$', deity_list_mobile,
        name='deity_list_mobile',
    ),
    # deities > detail
    url(
        r'^(?P<deity_slug>[^/]+)/$', deity_detail_mobile,
        name='deity_detail_mobile',
    ),
]
