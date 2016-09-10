from django.db import models

import sys, traceback
from . import court
from . import cite
from datetime import datetime


class Case(models.Model):
    case_name = models.CharField(max_length=200)
    topic = models.CharField(max_length=60) # tax, fraud, etc ENUM
    ruling = models.CharField(max_length=40) # change to ENUM
       # reversed and remanded, etc
    publication = models.CharField(max_length=50, null=True, blank=True)
    
    case_url = models.CharField(max_length=200,default="")
    decide_date = models.DateTimeField('date decided', null=True,blank=True)
    argue_date = models.DateTimeField('date argued', null=True,blank=True)
    case_below_cite = models.OneToOneField('Cite',null=True)
    case_court_below = models.OneToOneField('Court',null=True)
    docket = models.CharField(max_length=150, null=True, blank=True)
    plantiff = models.CharField(max_length=150, null=True, blank=True)
    defendant = models.CharField(max_length=150, null=True, blank=True)
    syllabus = models.TextField(null=True, blank=True)
    #
    # fill out case citation association table

    def __str__(self):              # __unicode__ on Python 2
        return self.case_name
    
    class Meta:
        db_table = 'Case'
        app_label = 'lawdb'
		
    def MultiStripString(self, indate):
        DATE_FORMATS = ['%B %d, %Y', '%b. %d, %Y']
        for date_format in DATE_FORMATS:
            try:
                outdate = datetime.strptime(indate, date_format)
            except ValueError:
                pass
            else:
                break
        else:
            outdate = None
		
        return outdate
  
    def loadFromCsv(self):  
        csvfile = open("C:/301Solutions/prototypes/webscraper/beautifulsoup/scotus_syllabus3.csv","r")
        
        first_word_topic = ""
        #now = datetime.datetime.now()
        header = csvfile.readline()
        for line in csvfile:
            parsed_line = line.replace("\n","")
            parsed_line = parsed_line.split("|")
            #fullName = parsed_line[0].split(" ")
            if (len(parsed_line) < 3):
                first_word_topic = " ".join(parsed_line)
                print("first_word_topic = "+first_word_topic)
            elif 'topic|casename, pubref,plantiff' not in line:
                try:
                    parsed_line[0] = first_word_topic+" "+str(parsed_line[0])
                    parsed_line[1] = parsed_line[1].replace("\t","")
                    parsed_line[1] = parsed_line[1].replace("(","")
                    parsed_line[1] = parsed_line[1].replace(")","")
                    parsed_line[1] = parsed_line[1][:199]
                    parsed_line[5] = parsed_line[5][:149]
                    parsed_line[3] = parsed_line[3][:149]
                    parsed_line[4] = parsed_line[4][:149]
                    parsed_line[2] = parsed_line[2][:49]
					
                    first_word_topic = ""
                    argued_date = parsed_line[6].replace("Argued:","")
                    argued_date = argued_date.strip()
                    print("argue date"+argued_date)
                    if "empty" in argued_date:
                        arg_date_object = None
                    else:
                        arg_date_object = self.MultiStripString(argued_date)
                    decided_date = parsed_line[7].replace("Decided:","")
                    decided_date = decided_date.strip()
                    if "empty" in decided_date:
                        decided_date_object = None 					
                    else:
                        dec_date_object = self.MultiStripString(decided_date)
                    
                    if (len(parsed_line) > 9):
                        c = Case(case_name=parsed_line[1], topic=parsed_line[0], ruling="empty", publication=parsed_line[2], \
                              case_url=parsed_line[9],decide_date=dec_date_object, argue_date=arg_date_object, \
                              docket=parsed_line[5],plantiff=parsed_line[3],defendant=parsed_line[4])
                    else:
                        c = Case(case_name=parsed_line[1], topic=parsed_line[0], ruling="empty", publication=parsed_line[2], \
                           case_url=parsed_line[8], docket=parsed_line[5],plantiff=parsed_line[3],defendant=parsed_line[4])
					
                    c.save()
                except Exception as e:
                    print ("Exception: "+line+"\n")
                    print ("e = {0}",sys.exc_info()[0])
                    traceback.print_exc()
                    sys.exit(-1)					
                    c1 = Case(case_name=parsed_line[1], topic=parsed_line[0], ruling="empty", publication=parsed_line[2], \
                           case_url=parsed_line[7], docket=parsed_line[5],plantiff=parsed_line[3],defendant=parsed_line[4])
                    c1.save()
					              
        csvfile.close()
                        
        
        

