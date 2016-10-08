from django.contrib import admin

# Register your models here.

from .models.case import Case
from .models.code import Code
from .models.opinion import Opinion
from .models.court import Court
from .models.courtAssignment import CourtAssignment
from .models.judge import Judge
from .models.lawSchool import LawSchool
from .models.legalPrinciple import LegalPrinciple
from .models.state import State
from .models.cite import Cite
from .models.casecite import CaseCite
from .models.casecode import CaseCode

class CourtAssignmentAdmin(admin.ModelAdmin):
    list_display = ('judge', 'court', 'start_date', 'end_date')
	
class CaseAdmin(admin.ModelAdmin):
    list_display = ['case_name', 'case_url', 'decide_date']
	
class CiteAdmin(admin.ModelAdmin):
    list_display = ['cite_name', 'url']
	
class CaseCiteAdmin(admin.ModelAdmin):
    list_display = ['case_link', 'cite_link']
	

admin.site.register(Case, CaseAdmin)
admin.site.register(Code)
admin.site.register(Opinion)
admin.site.register(Court)
admin.site.register(CourtAssignment, CourtAssignmentAdmin)
admin.site.register(Judge)
admin.site.register(LawSchool)
admin.site.register(LegalPrinciple)
admin.site.register(State)
admin.site.register(Cite, CiteAdmin)
admin.site.register(CaseCite, CaseCiteAdmin)
admin.site.register(CaseCode)


	
