from django.conf.urls.defaults import patterns, url

from poll.models import Poll


urlpatterns = patterns(
    '',
    url(
        r'^(?P<slug>[\w-]+)/$', 
        'jmbo.generic.views.generic_object_detail',
        {'queryset':Poll.permitted.all()},
        name='poll_object_detail'
    ),
)
