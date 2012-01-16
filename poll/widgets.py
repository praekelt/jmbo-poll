from django.forms.widgets import RadioFieldRenderer as BaseRadioFieldRenderer
from django.forms.widgets import RadioSelect as BaseRadioSelect
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

class RadioFieldRenderer(BaseRadioFieldRenderer):
    """Use div tags instad of a ul tag for rendering"""

    def render(self):
        return mark_safe(u'\n'.join([u'<div>%s</div>'
            % force_unicode(w) for w in self]))


class RadioSelect(BaseRadioSelect):
    renderer = RadioFieldRenderer
