from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.contrib import messages

from poll.models import Poll
from poll.forms import PollVoteForm


def poll_vote(request, poll_id, template):
    poll = get_object_or_404(Poll, id=poll_id)
    if request.method == 'POST':
        form = PollVoteForm(request.POST, request=request, poll=poll)
        if form.is_valid():
            form.save()
            msg = _("Your vote has been saved")
            messages.success(request, msg, fail_silently=True)

        # If we're posting from a widget but the post is not by ajax then
        # we have to switch to the detail template.
        if (template == 'poll/poll_widget.html') and not request.is_ajax():
            template = 'poll/poll_detail.html'
    else:
        form = PollVoteForm(request=request, poll=poll)

    extra = dict(form=form, object=poll, view_modifier=None)
    return render_to_response(template, extra, context_instance=RequestContext(request))
