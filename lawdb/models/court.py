from django.db import models

from . import state

class Court(models.Model):
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=200)
    state = models.ForeignKey('State')
    hierachy_level = models.PositiveSmallIntegerField() # smaller is lower

    lower_court = models.OneToOneField('self', related_name = 'inferior_court')
    upper_court = models.OneToOneField('self', related_name = 'superior_court')

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

    TRAIL = 'trial'
    APPELLATE = 'apel'
    COURT_TYPE_CHOICES = (
        (FEDERAL, 'Trial'),
        (STATE, 'Appellate'),
    )
    court_type = models.CharField(
        max_length=1,
        choices=COURT_TYPE_CHOICES,
    )

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    class Meta:
        db_table = 'Court'
        app_label = 'lawdb'
    
    
