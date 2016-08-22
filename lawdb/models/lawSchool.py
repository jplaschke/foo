from django.db import models

class LawSchool(models.Model):
    name = models.CharField(max_length=40)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)    
        
    def __str__(self):              # __unicode__ on Python 2
        return self.name

    class Meta:
        db_table = 'LawSchool'
        app_label = 'lawdb'
