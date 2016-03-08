from django.conf.urls import patterns, url
from .views import index_mobile


app_name = 'index'
urlpatterns = [
    # index
    url(
        r'^$', index_mobile,
        name='index_mobile',
    ),
]
