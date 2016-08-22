from django.db import models

from . import judge
from . import legalPrinciple

class Opinion(models.Model):
    judge = models.ManyToManyField('Judge')
    for_plantiff = models.PositiveSmallIntegerField(default=0)
    for_defendant = models.PositiveSmallIntegerField(default=0)
    #majority
    #concurrence, Plurality opinion
    #dissent, per curiam, unanimous, etc
    opinion_type = models.CharField(max_length=30, default="") # change to enum 
    opinion_text = models.TextField(null=True)

    # a case can have many opinions (1 to n)
    case_opinion = models.ForeignKey('Case', null=True)

    legal_principle = models.ForeignKey('LegalPrinciple')
   

#    def __str__(self):              # __unicode__ on Python 2
#        return self.case_name
    

    class Meta:
        db_table = 'Opinion'
        app_label = 'lawdb'
