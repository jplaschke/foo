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


class CourtAssignmentAdmin(admin.ModelAdmin):
    list_display = ('judge', 'court', 'start_date', 'end_date')
	
admin.site.register(Case)
admin.site.register(Code)
admin.site.register(Opinion)
admin.site.register(Court)
admin.site.register(CourtAssignment, CourtAssignmentAdmin)
admin.site.register(Judge)
admin.site.register(LawSchool)
admin.site.register(LegalPrinciple)
admin.site.register(State)


	
