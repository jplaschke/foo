from django.db import models
import sys, traceback
from django.db.models import Q

from . import cite
from . import case

class CaseCite(models.Model):
    cite_link = models.ForeignKey('Cite')
    case_link = models.ForeignKey('Case') 
    for_plantiff = models.PositiveSmallIntegerField(default=0)
    for_defendant = models.PositiveSmallIntegerField(default=0)

    def __str__(self):              # __unicode__ on Python 2
        return "Case Cite Association"
    
    class Meta:
        db_table = 'CaseCite'
        app_label = 'lawdb'

    def loadFromCsv(self):
        csvfile = open("C:/301Solutions/prototypes/webscraper/beautifulsoup/scotus_cite.csv","r")
        header = csvfile.readline()
        for line in csvfile:
            parsed_line = line.split("|")
            if (len(parsed_line) < 3):
                print ("ERROR parsed_line too short")
                print (line)
                #sys.exit(-2)
            else:
                cite_name = parsed_line[0]
                cite_url = parsed_line[1]
                case_url = parsed_line[2]
                topic = parsed_line[3]
                topic = topic.strip()
                cite_url = cite_url.strip()
                case_url = case_url.strip()
                cite_name = cite_name.strip()
                print ("cite_url = "+str(cite_url))
                print ("cite_url = "+str(len(cite_url)))
                print ("topic = "+topic)
                print ("case_url = "+case_url)
                try:
                    if ("ZS.html" in case_url):
                        citeEntry = cite.Cite(cite_name = cite_name, url = cite_url)
                        citeEntry.save() 
                        # look for case_url
                        try: 
                            obj = case.Case.objects.get(Q(case_url__contains=case_url), Q(topic__contains=topic))
                            cs = CaseCite(cite_link=citeEntry, case_link=obj)
                            cs.save()
                        except:
                            # we have no object!  do something
                            print ("could not find "+case_url)
                            #sys.exit(-1)                        
                except:
                    print ("Exception: "+line+"\n")
                    print ("e = {0}",sys.exc_info()[0])
                    traceback.print_exc()
                    sys.exit(-1)            
                
        csvfile.close()
                        
        
                