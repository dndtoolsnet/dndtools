from django.conf.urls import patterns, url
from .views import skill_list, skill_detail, skills_in_rulebook


app_name = 'skills'
urlpatterns = [
    # skills
    url(r'^$', skill_list, name='skill_list'),

    # skills > detail
    url(r'^(?P<skill_slug>[^/]+)/$', skill_detail, name='skill_detail'),

    # skills > detail (variant)
    url(r'^(?P<rulebook_slug>[^/]+)--(?P<rulebook_id>\d+)/(?P<skill_slug>[^/]+)/$',
        skill_detail, name='skill_variant_detail'),

    # skills > rulebook
    url(r'^rulebook/(?P<rulebook_slug>[^/]+)--(?P<rulebook_id>\d+)/$',
        skills_in_rulebook, name='skills_in_rulebook')
]
