from django.conf.urls import patterns, url

from jmbo.views import ObjectDetail

from poll.models import Poll


urlpatterns = patterns(
    '',
    url(
        r'^(?P<slug>[\w-]+)/$',
        ObjectDetail.as_view(),
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
