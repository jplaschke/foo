from django.db import models


class LegalPrinciple(models.Model):
    name = models.CharField(max_length=75)
    definition = models.CharField(max_length=90)

    class Meta:
        db_table = 'LegalPrinciple'
        app_label = 'lawdb'
