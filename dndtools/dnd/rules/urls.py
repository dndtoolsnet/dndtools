from django.conf.urls import patterns, url
from .views import rule_list, rule_detail


app_name = 'rules'
urlpatterns = [
    # rules list
    url(r'^$', rule_list, name='rule_list'),

    # rules
    url(r'^(?P<rulebook_slug>[^/]+)--(?P<rulebook_id>\d+)/(?P<rule_slug>[^/]+)--(?P<rule_id>\d+)/$',
        rule_detail, name='rule_detail')
]
