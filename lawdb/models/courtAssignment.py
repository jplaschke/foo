from django.db import models

from . import court
from . import judge
import datetime

class CourtAssignment(models.Model):
    start_date = models.PositiveSmallIntegerField(null=True)
    end_date = models.PositiveSmallIntegerField(null=True)
    court =  models.ForeignKey('Court')
    judge = models.ForeignKey('Judge')

    class Meta:
        db_table = 'CourtAssignment'
        app_label = 'lawdb'

		
    
    def loadFromCsv(self):
        csvfile = open("C:/301Solutions/prototypes/webscraper/beautifulsoup/justices.csv","r")
		
        now = datetime.datetime.now()
		
        c = court.Court.objects.get(name="Supreme Court")

        for line in csvfile:
            parsed_line = line.split(",")
            fullName = parsed_line[0].split(" ")
            if ((len(fullName) > 1) and (len(parsed_line) > 3)):
                if (len(fullName) > 3):
                    last_name = fullName[-1]
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
                    state_born = (parsed_line[2])
                i = 2
                if ('Jr.' in parsed_line[1]):
                    i = 3
                start_year = int(parsed_line[i])
                if ("present" in parsed_line[i+1]):
                    end_year = int(now.year)
                else:
                    end_year = int(parsed_line[i+1])
                print("line = "+line+"\n")
                j_qs = judge.Judge.objects.filter(first_name=first_name, last_name=last_name)
                for j in j_qs:
                    ca = CourtAssignment(start_date=start_year, end_date=end_year, court=c, judge=j)
                ca.save()
        csvfile.close()
            			
		
