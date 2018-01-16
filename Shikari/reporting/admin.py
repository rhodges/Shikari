from django.contrib import admin
from .models import *
from Shikari.admin import TextField2TextInput

class ReportedHoursAdmin(TextField2TextInput):
    list_display = ('person', 'role', 'hours', 'date', 'task')
    list_filter = ['person', 'role', 'hours', 'date', 'task']
    search_fields = ('person', 'role', 'date', 'task', 'notes')
    verbose_name_plural = 'Reported Hours'
    fieldsets = (
        ('Worker', {
            'fields': ('person', 'role')
        }),
        ('Hours', {
            'fields': ('hours', 'date')
        }),
        (None, {
            'fields': ('task',)
        }),
        (None, {
            'fields': ('notes',)
        }),
    )

admin.site.register(ReportedHours, ReportedHoursAdmin)
