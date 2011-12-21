from django import template

register = template.Library()


@register.inclusion_tag(
    'poll/inclusion_tags/poll_detail.html',
    takes_context=True
)
def poll_detail(context, obj):
    context.update({
        'object': obj,
        'can_vote': obj.can_vote(context['request'])
        })  
    return context
