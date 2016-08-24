from django.db import models

from . import case
from . import cite

class CaseCite(models.Model):
    cite_link = models.ForeignKey('Cite')
    case_link = models.ForeignKey('Case') 
    for_plantiff = models.PositiveSmallIntegerField(default=0)
    for_defendant = models.PositiveSmallIntegerField(default=0)

    def __str__(self):              # __unicode__ on Python 2
        return "Case Cite Association"
    
    class Meta:
        db_table = 'CaseCite'
        app_label = 'lawdb'
