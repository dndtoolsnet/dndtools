from django.conf.urls import patterns, url
from .views import rule_detail_mobile


app_name = 'rules'
urlpatterns = [
    # rules
    url(
        r'^(?P<rulebook_slug>[^/]+)--(?P<rulebook_id>\d+)/(?P<rule_slug>[^/]+)--(?P<rule_id>\d+)/$', rule_detail_mobile,
        name='rule_detail_mobile',
    ),
]
