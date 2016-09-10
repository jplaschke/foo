from django.db import models
import datetime
from . import lawSchool

class Judge(models.Model):
    first_name = models.CharField(max_length=25)
    middle_name = models.CharField(max_length=25,null=True,blank=True)
    last_name = models.CharField(max_length=25)
    year_born = models.PositiveSmallIntegerField(null=True)
    state_born = models.CharField(max_length=2,null=True)
    law_school = models.ForeignKey('LawSchool',null=True, blank=True)   

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
        unique_together = ('first_name', 'last_name', 'state_born')
        

    def loadFromCsv(self):
        csvfile = open("C:/301Solutions/prototypes/webscraper/beautifulsoup/justices.csv","r")
		
        now = datetime.datetime.now()

        for line in csvfile:
            parsed_line = line.split(",")
            fullName = parsed_line[0].split(" ")
            if (len(fullName) > 1):
                if (len(fullName) > 3):
                    last_name = fullName[-1]
                    middle_name = fullName[1]
                elif (len(fullName) > 2):
                    if ((fullName[1] == 'Van') or (fullName[1] == 'De')):
                        last_name = fullName[1]+" "+fullName[2]
                    else:
                        last_name = fullName[2] 
                    first_name = fullName[0]
                else:
                    first_name = fullName[0]
                    last_name = fullName[1]
                print ("state_born = "+str(parsed_line))
                if (len(parsed_line) < 5) and (len(parsed_line) > 0): 
                    state_born = parsed_line[1]
                elif (len(parsed_line) > 1):
                    state_born = parsed_line[2]
                try:
                    j = Judge(first_name=first_name, last_name=last_name, year_born=9999, state_born=state_born)
                    j.save()
                except:
                    print ("Exception: "+first_name+" "+last_name+"\n")
                
        csvfile.close()
            			
		
		