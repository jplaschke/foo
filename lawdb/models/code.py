from django.db import models

from . import state

class Code(models.Model):
    title = models.CharField(max_length=75)
    chapter = models.CharField(max_length=10)
    section = models.PositiveSmallIntegerField()
    subtitle = models.CharField(max_length=10)
    topic = models.CharField(max_length=10)
    url =  models.CharField(max_length=80)
    
    FEDERAL = 'Fed'
    STATE = 'State'
    FED_STATE_CHOICES = (
        (FEDERAL, 'Federal'),
        (STATE, 'State'),
    )
    fed_or_state = models.CharField(
        max_length=1,
        choices=FED_STATE_CHOICES,
    )

    state = models.ForeignKey('State')
    
    def __str__(self):              # __unicode__ on Python 2
        return self.title

    class Meta:
        db_table = 'Code'
        app_label = 'lawdb'
