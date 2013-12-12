from django import template
from django.core.urlresolvers import reverse

from poll.forms import PollVoteForm


register = template.Library()


@register.inclusion_tag(
    'poll/inclusion_tags/poll_detail.html',
    takes_context=True
)
def poll_detail(context, obj):
    can_vote_on_poll, reason = obj.can_vote_on_poll(context['request'])
    context.update({
        'object': obj,
        'can_vote_on_poll': can_vote_on_poll,
        'reason': reason
        })
    if can_vote_on_poll and not context.has_key('form'):
        context['form'] = PollVoteForm(request=context['request'], poll=obj)
    return context


@register.inclusion_tag(
    'poll/inclusion_tags/poll_widget.html',
    takes_context=True
)
def poll_widget(context, obj):
    return poll_detail(context, obj)
