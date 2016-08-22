from django.db import models

from . import lawSchool

class Judge(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=25)
    year_born = models.PositiveSmallIntegerField()
    state_born = models.CharField(max_length=2)
    law_school = models.ForeignKey('LawSchool')    

    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
    )

    def __str__(self):              # __unicode__ on Python 2
        return self.first_name + " " + self.last_name

    class Meta:
        db_table = 'Judge'
        app_label = 'lawdb'
        
