from django.db import models

from . import court
from . import cite

class Case(models.Model):
    case_name = models.CharField(max_length=200)
    topic = models.CharField(max_length=20) # tax, fraud, etc ENUM
    ruling = models.CharField(max_length=40) # change to ENUM
       # reversed and remanded, etc
    
    case_url = models.CharField(max_length=200,default="")
    decide_date = models.DateTimeField('date decided')
    argue_date = models.DateTimeField('date argued')
    case_below_cite = models.OneToOneField('Cite')
    case_court_below = models.OneToOneField('Court')
    docket = models.CharField(max_length=50)
    plantiff = models.CharField(max_length=50)
    defendant = models.CharField(max_length=50)
    syllabus = models.TextField
    #
    # fill out case citation association table

    def __str__(self):              # __unicode__ on Python 2
        return self.case_name
    
    class Meta:
        db_table = 'Case'
        app_label = 'lawdb'

