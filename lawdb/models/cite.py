from django.db import models


class Cite(models.Model):
    cite_name = models.CharField(max_length=20)
    url = models.CharField(max_length=50) 
    

    def __str__(self):              # __unicode__ on Python 2
        return self.cite_name
    
    class Meta:
        db_table = 'Cite'
        app_label = 'lawdb'
