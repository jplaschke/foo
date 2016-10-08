from django.db import models
import sys, traceback
from django.db.models import Q

from . import code
from . import case

class CaseCode(models.Model):
    code_link = models.ForeignKey('Code')
    case_link = models.ForeignKey('Case') 
    
    def __str__(self):              # __unicode__ on Python 2
        return "Case: "+self.case_link.case_name+" "+"Code: "+"Title "+self.code_link.title+" Section "+self.code_link.section 
    
    class Meta:
        db_table = 'CaseCode'
        app_label = 'lawdb'
        unique_together = ("code_link", "case_link")

    def loadFromCsv(self):
        csvfile = open("C:/301Solutions/prototypes/webscraper/beautifulsoup/scotus_code.csv","r")
        header = csvfile.readline()
        for line in csvfile:
            parsed_line = line.split("|")
            if (len(parsed_line) < 3):
                print ("ERROR parsed_line too short = "+line)
                #sys.exit(-2)
            elif parsed_line[0] == "Code":
                code_full_name = parsed_line[1]
                code_url = parsed_line[2]
                case_url = parsed_line[3]
                topic = parsed_line[4]
                topic = topic.strip()
                case_url = case_url.strip()
                code_url = code_url.strip()
                print ("code_full_name = "+code_full_name)
                code_parsed = code_full_name.split(" ")
                print ("code_parsed = "+repr(code_parsed))
                title = code_parsed[0]
                code_name = code_parsed[1]
                #chapter = models.CharField(max_length=10)
                
                section = (code_parsed[2])
                section = section.strip()
                print ("section = "+section)
                try:
                    section = (section.strip())
                except:
                    section = (code_parsed[-1])
                    print ("2section = "+section)
                    section = (section.strip())
                print ("title = "+str(title))
                print ("code_url = "+str(code_url))
                print ("topic = "+topic)
                print ("case_url = "+case_url)
                try:
                    codeEntry = code.Code.objects.get(Q(title=title), Q(code_name=code_name), Q(section=section))
                except:
                    codeEntry = None
               
                try:
                    if codeEntry is None:
                        codeEntry = code.Code(title = title, url = code_url, code_name=code_name, section=section, \
					                 topic=topic, fed_or_state=code.Code.FEDERAL)
                        codeEntry.save() 
                    # look for case_url
                    try: 
                        obj = case.Case.objects.get(Q(case_url=case_url), Q(topic=topic))
                        cs = CaseCode(code_link=codeEntry, case_link=obj)
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
            			
		
				