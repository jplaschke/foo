from django.db import models

from . import state

class Code(models.Model):
    title = models.CharField(max_length=75, null=False) 
    code_name = models.CharField(max_length=30, null=True,blank=True)
    chapter = models.CharField(max_length=10, null=True,blank=True)
    section = models.CharField(max_length=9, null=True,blank=True)
    subtitle = models.CharField(max_length=10, null=True,blank=True)
    topic = models.CharField(max_length=50, null=True,blank=True)
    url =  models.CharField(max_length=80, null=True,blank=True)
    year = models.PositiveSmallIntegerField( null=True,blank=True)
    
    FEDERAL = 'Fed'
    STATE = 'State'
    FED_STATE_CHOICES = (
        (FEDERAL, 'Federal'),
        (STATE, 'State'),
    )
    fed_or_state = models.CharField(
        max_length=7,
        choices=FED_STATE_CHOICES,
    )

    state = models.ForeignKey('State', null=True, blank=True)
    
    def __str__(self):              # __unicode__ on Python 2
        return "Title "+self.title+" Section "+self.section

    class Meta:
        db_table = 'Code'
        app_label = 'lawdb'
        unique_together = ("title", "code_name","chapter","section")
