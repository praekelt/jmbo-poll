from django.db import models
from django.db.models.aggregates import Sum

from secretballot.models import Vote

from jmbo.models import ModelBase


class Poll(ModelBase):
    target = models.ManyToManyField(
        ModelBase,
        null=True,
        blank=True,
        related_name='poll_target'
    )
    
    def can_vote(self, request):
        # Return tuple so API remains consistent with what Jmbo dictates
        return 'dc', Vote.objects.filter(
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

    def percentage(self):
        total = Vote.objects.filter(
            object_id__in=[o.id for o in self.poll.polloption_set.all()]
        ).aggregate(Sum('vote'))['vote__sum'] or 0

        if total:
            votes = Vote.objects.filter(
                object_id=self.id
            ).aggregate(Sum('vote'))['vote__sum'] or 0
            return votes * 100.0 / total
        return 0
            
