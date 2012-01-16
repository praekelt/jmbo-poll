from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType

from secretballot.views import vote
from jmbo.forms import as_div

from poll.models import PollOption
from poll.widgets import RadioSelect


class PollVoteForm(forms.Form):
    poll_option = forms.ChoiceField(choices=[], required=True, widget=RadioSelect)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        self.poll = kwargs.pop('poll')
        super(PollVoteForm, self).__init__(*args, **kwargs)

        self.fields['poll_option'].label = ''        
        self.fields['poll_option'].choices = \
            [(o.id, o.title) for o in self.poll.polloption_set.all()]

    def clean(self):
        if not self.poll.can_vote(self.request):
            raise forms.ValidationError(
                _("You are not allowed to vote on this poll.")
            )
        return super(PollVoteForm, self).clean()

    def save(self): 
        poll_option = self.cleaned_data['poll_option']
        content_type = ContentType.objects.get(app_label='poll', model='polloption')
        vote(self.request, content_type, poll_option, 1)

    as_div = as_div
