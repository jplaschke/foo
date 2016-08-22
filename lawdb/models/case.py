from django.db import models

from . import court
from . import opinion

class Case(models.Model):
    case_name = models.CharField(max_length=200)
    topic = models.CharField(max_length=20) # tax, fraud, etc ENUM
    ruling = models.CharField(max_length=40) # change to ENUM
       # reversed and remanded, etc
    
    # court = 
    decide_date = models.DateTimeField('date decided')
    argue_date = models.DateTimeField('date argued')
    case_below_cite = models.OneToOneField('Opinion', related_name='case_below_cite')
    case_court_below = models.OneToOneField('Court')
    docket = models.CharField(max_length=50)
    plantiff = models.CharField(max_length=50)
    defendant = models.CharField(max_length=50)
    syllabus = models.TextField
    #
    citations = models.ManyToManyField('self')
    
    #code = many to many


    def __str__(self):              # __unicode__ on Python 2
        return self.case_name
    
    class Meta:
        db_table = 'Case'
        app_label = 'lawdb'

