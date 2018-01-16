from django.contrib import admin
from .models import *
from Shikari.admin import TextField2TextInput

admin.site.register(Project, TextField2TextInput)
admin.site.register(MilestoneType, TextField2TextInput)
admin.site.register(Milestone, TextField2TextInput)
admin.site.register(Role, TextField2TextInput)
admin.site.register(Assignment, TextField2TextInput)
admin.site.register(ProposedHours, TextField2TextInput)
