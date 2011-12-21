from django.db import models

from secretballot.models import Vote

from jmbo.models import ModelBase


class Poll(ModelBase):
    target = models.ManyToManyField(
        ModelBase,
        related_name='poll_target'
    )
    
    def can_vote(self, request):
        return Vote.objects.filter(
            object_id__in=[o.id for o in self.polloption_set.all()],
            token=request.secretballot_token
        ).count() == 0

        
class PollOption(models.Model):
    title = models.CharField(max_length=255)
    poll = models.ForeignKey(
        Poll,
    )
    is_correct_answer = models.BooleanField(
        default=False, help_text="Is this option the correct answer?"
    )
        
    def __unicode__(self):
        return "%s - %s" % (self.poll.title, self.title)
