from django.db import models

from . import court
from . import judge

class CourtAssignment(models.Model):
    start_date = models.DateTimeField('date stared')
    end_date = models.DateTimeField('date ended')
    court =  models.ForeignKey('Court')
    judge = models.ForeignKey('Judge')

    class Meta:
        db_table = 'CourtAssignment'
        app_label = 'lawdb'
