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
    url(
        r'^poll-vote/(?P<poll_id>\d+)/$', 
        'poll.views.poll_vote', 
        {},
        name='poll-vote'
    ), 
)
