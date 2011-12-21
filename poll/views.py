from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _

from poll.models import Poll
from poll.forms import PollVoteForm


def poll_vote(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    if request.method == 'POST':
        form = PollVoteForm(request.POST, request=request, poll=poll) 
        if form.is_valid():
            form.save()
            request.user.message_set.create(
                message=_("Your vote has been saved")
            )
    else:
        form = PollVoteForm(request=request, poll=poll) 

    extra = dict(form=form, object=poll, view_modifier=None)
    return render_to_response('poll/poll_detail.html', extra, context_instance=RequestContext(request))
