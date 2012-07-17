from django import forms
from django.contrib import admin
from jmbo.admin import ModelBaseAdmin
from poll.models import Poll, PollOption

readonly_attrs = {
    'readonly': 'readonly',
    'style': 'border-width: 0px;',
}


class PollOptionForm(forms.ModelForm):
    votes = forms.IntegerField(
        required=False,
        help_text='Number of votes cast for this option.',
        widget=forms.TextInput(attrs=readonly_attrs),
        initial='',
    )
    percentage = forms.FloatField(
        required=False,
        help_text='Percentage of votes cast for this option in '
                  'relation to all of the other options.',
        widget=forms.TextInput(attrs=readonly_attrs),
    )

    class Meta:
        model = PollOption

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        self.base_fields['votes'].initial = instance.vote_count if \
            instance else ''
        self.base_fields['percentage'].initial = instance.percentage if \
            instance else ''
        super(PollOptionForm, self).__init__(*args, **kwargs)


class PollOptionInline(admin.StackedInline):
    model = PollOption
    form = PollOptionForm


class PollAdmin(ModelBaseAdmin):
    inlines = [PollOptionInline]

admin.site.register(Poll, PollAdmin)
