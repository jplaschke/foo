from django.db import models


class State(models.Model):
    name = models.CharField(max_length=75)
    abbreiviation = models.CharField(max_length=2)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name

    class Meta:
        db_table = 'State'
        app_label = 'lawdb'
