from django.contrib import admin
from .models import *
from django.forms.widgets import TextInput

class TextField2TextInput(admin.ModelAdmin):
    # I like to use TextFields to avoid restricting character counts, but I like TextInput widget
    formfield_overrides = {
        models.TextField: {'widget': TextInput},
    }

class TextField2TextInputInline(admin.TabularInline):
    # I like to use TextFields to avoid restricting character counts, but I like TextInput widget
    formfield_overrides = {
        models.TextField: {'widget': TextInput},
    }

class OrganizationWebsiteInline(TextField2TextInputInline):
    model = OrganizationWebsite
    fields = ('website', 'site_type')
    extra = 0
    verbose_name_plural = 'Websites'

class OrganizationAdmin(TextField2TextInput):
    list_display = ('name', 'is_home')
    list_filter = ['is_home', 'name']
    search_fields = ('name',)
    verbose_name_plural = 'Oranizations'
    inlines = [
        OrganizationWebsiteInline,
    ]

admin.site.register(Organization, OrganizationAdmin)
admin.site.register(WebsiteType, TextField2TextInput)
admin.site.register(OrganizationWebsite, TextField2TextInput)

class PhoneNumberInline(TextField2TextInputInline):
    model = PhoneNumber
    fields = ('number', 'contact_type', 'is_primary',)
    extra = 1
    verbose_name_plural = 'Phone Numbers'
    formfield_overrides = {
        models.TextField: {'widget': TextInput},
    }

class EmailAddressInline(TextField2TextInputInline):
    model = EmailAddress
    fields = ('email', 'contact_type', 'is_primary',)
    extra = 1
    verbose_name_plural = 'Email Addresses'

class PersonAdmin(TextField2TextInput):
    list_display = ('last_name', 'first_name', 'name_suffix', 'job_title', 'organization')
    list_filter = ('last_name', 'first_name', 'name_suffix', 'job_title', 'organization')
    search = ('last_name', 'first_name', 'middle_name', 'name_suffix', 'job_title', 'organization', 'manager', 'notes')
    verbose_name_plural = 'People'
    fieldsets = (
        (None, {
            'fields': ('user',)
        }),
        ('Name', {
            # 'classes': ('citation-ref-type',),
            'fields': ('name_prefix', 'first_name', 'middle_name', 'last_name', 'name_suffix')
        }),
        ('Organization', {
            'fields': ('organization', 'job_title', 'job_class', 'manager')
        }),
        (None, {
            'fields': ('notes',)
        }),
    )
    inlines = [
        PhoneNumberInline,
        EmailAddressInline,
    ]

admin.site.register(Person, PersonAdmin)
admin.site.register(PhoneContactType, TextField2TextInput)
admin.site.register(EmailContactType, TextField2TextInput)
admin.site.register(PhoneNumber, TextField2TextInput)
admin.site.register(EmailAddress, TextField2TextInput)
