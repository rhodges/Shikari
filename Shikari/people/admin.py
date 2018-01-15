from django.contrib import admin
from .models import *

class OrganizationWebsiteInline(admin.TabularInline):
    model = OrganizationWebsite
    fields = ('website', 'site_type')
    extra = 0
    # classes = ['collapse', 'open']
    verbose_name_plural = 'Websites'
    def formfield_for_dbfield(self, db_field, **kwargs):
        from django.forms.widgets import TextInput
        if db_field.name in ['site_type']:
            kwargs['widget'] = TextInput
        return super(OrganizationWebsiteInline,self).formfield_for_dbfield(db_field, **kwargs)

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_home')
    list_filter = ['is_home', 'name']
    search_fields = ('name',)
    verbose_name_plural = 'Oranizations'
    def formfield_for_dbfield(self, db_field, **kwargs):
        from django.forms.widgets import TextInput
        if db_field.name in ['name']:
            kwargs['widget'] = TextInput
        return super(OrganizationAdmin,self).formfield_for_dbfield(db_field, **kwargs)
    inlines = [
        OrganizationWebsiteInline,
    ]

admin.site.register(Organization, OrganizationAdmin)
admin.site.register(WebsiteType)
admin.site.register(OrganizationWebsite)

class PhoneNumberInline(admin.TabularInline):
    model = PhoneNumber
    fields = ('number', 'contact_type', 'is_primary',)
    extra = 1
    verbose_name_plural = 'Phone Numbers'
    def formfield_for_dbfield(self, db_field, **kwargs):
        from django.forms.widgets import TextInput
        if db_field.name in ['number']:
            kwargs['widget'] = TextInput
        return super(PhoneNumberInline,self).formfield_for_dbfield(db_field, **kwargs)

class EmailAddressInline(admin.TabularInline):
    model = EmailAddress
    fields = ('email', 'contact_type', 'is_primary',)
    extra = 1
    verbose_name_plural = 'Email Addresses'
    def formfield_for_dbfield(self, db_field, **kwargs):
        from django.forms.widgets import TextInput
        if db_field.name in ['email']:
            kwargs['widget'] = TextInput
        return super(EmailAddressInline,self).formfield_for_dbfield(db_field, **kwargs)

class PersonAdmin(admin.ModelAdmin):
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
    def formfield_for_dbfield(self, db_field, **kwargs):
        from django.forms.widgets import TextInput
        if db_field.name in ['name_prefix', 'first_name', 'middle_name', 'last_name', 'name_suffix', 'job_title', 'job_class']:
            kwargs['widget'] = TextInput
        return super(PersonAdmin,self).formfield_for_dbfield(db_field, **kwargs)
    inlines = [
        PhoneNumberInline,
        EmailAddressInline,
    ]

admin.site.register(Person, PersonAdmin)
admin.site.register(PhoneContactType)
admin.site.register(EmailContactType)
admin.site.register(PhoneNumber)
admin.site.register(EmailAddress)
