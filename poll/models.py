from django.db import models

from jmbo.models import ModelBase


class Poll(ModelBase):
    target = models.ManyToManyField(
        ModelBase,
        related_name='poll_target'
    )
    
        
class PollOption(models.Model):
    title = models.CharField(max_length=255)
    poll = models.ForeignKey(
        Poll,
#        related_name='poll_options'
    )
    is_correct_answer = models.BooleanField(
        default=False, help_text="Is this option the correct answer?"
    )
        
    def __unicode__(self):
        return "%s - %s" % (self.poll.title, self.title)
