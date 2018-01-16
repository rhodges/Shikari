from django.contrib import admin
from django.db import models
from django.forms.widgets import TextInput, Textarea

class TextField2TextInput(admin.ModelAdmin):
    # I like to use TextFields to avoid restricting character counts, but I like TextInput widget
    formfield_overrides = {
        models.TextField: {'widget': TextInput},
    }
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ['notes', 'description']:
            kwargs['widget'] = Textarea
        return super(TextField2TextInput,self).formfield_for_dbfield(db_field, **kwargs)

class TextField2TextInputInline(admin.TabularInline):
    # I like to use TextFields to avoid restricting character counts, but I like TextInput widget
    formfield_overrides = {
        models.TextField: {'widget': TextInput},
    }
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ['notes', 'description']:
            kwargs['widget'] = Textarea
        return super(TextField2TextInputInline,self).formfield_for_dbfield(db_field, **kwargs)
