from django.conf.urls import patterns, url
from  .views import language_index_mobile, language_detail_mobile


app_name = 'languages'
urlpatterns = [
    # languages
    url(
        r'^$', language_index_mobile,
        name='language_index_mobile'
    ),
    # languages > detail
    url(
        r'^(?P<language_slug>[^/]+)/$', language_detail_mobile,
        name='language_detail_mobile'
    ),
]
