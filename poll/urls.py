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
        r'^poll-detail-vote/(?P<poll_id>\d+)/$', 
        'poll.views.poll_vote', 
        {'template':'poll/poll_detail.html'},
        name='poll-detail-vote'
    ), 
    url(
        r'^poll-widget-vote/(?P<poll_id>\d+)/$', 
        'poll.views.poll_vote', 
        {'template':'poll/poll_widget.html'},
        name='poll-widget-vote'
    ), 

)
