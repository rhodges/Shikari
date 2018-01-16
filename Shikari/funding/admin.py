from django.contrib import admin
from .models import *
from Shikari.admin import TextField2TextInput

admin.site.register(FundingType, TextField2TextInput)
admin.site.register(Funding, TextField2TextInput)
admin.site.register(Task, TextField2TextInput)
