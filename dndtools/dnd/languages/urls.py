from django.conf.urls import patterns, url
from .views import language_index, language_detail


app_name = 'languages'
urlpatterns = [
    # languages
    url(r'^$', language_index, name='language_index'),

    # languages > detail
    url(r'^(?P<language_slug>[^/]+)/$', language_detail, name='language_detail'),
]
