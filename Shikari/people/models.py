from django.db import models

########################################################################
#  ORGANIZATION
########################################################################

class Organization(models.Model):
    is_home = models.BooleanField(verbose_name='Home Organization', default=False)
    name = models.TextField(verbose_name='Org. Name')

    def __str__(self):
        return self.name

class WebsiteType(models.Model):
    site_type = models.TextField(verbose_name='Site Type')
    display_order = models.IntegerField()

    class Meta:
        ordering = ['display_order']
        app_label="people_meta"
        verbose_name="Website Type"
        verbose_name_plural="Website Types"

    def __str__(self):
        return self.site_type

class OrganizationWebsite(models.Model):
    website = models.URLField(max_length=254, verbose_name='URL')
    site_type = models.ForeignKey(WebsiteType, models.SET_NULL, null=True, blank=True, default=None)
    organization = models.ForeignKey(Organization, models.CASCADE)

    def __str__(self):
        return self.website

    class Meta:
        app_label="people_meta"
        verbose_name="Organization Website"
        verbose_name_plural="Organization Websites"

########################################################################
#  Person
########################################################################

class Person(models.Model):
    from django.contrib.auth.models import User
    first_name = models.TextField(verbose_name='First Name', null=True, blank=True, default=None)
    last_name = models.TextField(verbose_name='Last Name')
    middle_name = models.TextField(verbose_name='Middle Name', null=True, blank=True, default=None)
    name_prefix = models.TextField(verbose_name='Name Prefix', null=True, blank=True, default=None)
    name_suffix = models.TextField(verbose_name='Name Suffix', null=True, blank=True, default=None)
    organization = models.ForeignKey(Organization, models.SET_NULL, null=True, blank=True, default=None)
    user = models.ForeignKey(User, models.SET_NULL, null=True, blank=True, default=None)
    job_title = models.TextField(verbose_name='Job Title', null=True, blank=True, default=None)
    job_class = models.TextField(verbose_name='Job Class', null=True, blank=True, default=None)
    manager = models.ForeignKey("self", models.SET_NULL, verbose_name='Reports To', null=True, blank=True, default=None)
    notes = models.TextField(verbose_name="Additional Notes", null=True, blank=True, default=None)

    def __str__(self):
        name_array = []
        potentials_array = [self.name_prefix, self.first_name, self.middle_name, self.last_name, self.name_suffix]
        for name_part in potentials_array:
            if name_part:
                name_array.append(name_part)

        if self.job_title:
            return "%s: %s" % (' '.join(name_array), self.job_title)
        else:
            return ' '.join(name_array)

    class Meta:
        ordering = ['last_name']
        verbose_name = 'Person'
        verbose_name_plural = 'People'

class ContactMethod(models.Model):
    is_primary = models.BooleanField(default=False, verbose_name='Primary Contact')
    person = models.ForeignKey(Person, models.CASCADE)
    # display_order = models.IntegerField()
    #
    # class Meta:
    #     ordering = ['display_order']

class PhoneContactType(models.Model):
    contact_type = models.TextField(verbose_name='Type')
    display_order = models.IntegerField(default=100)

    def __str__(self):
        return self.contact_type

    class Meta:
        ordering = ['display_order']
        app_label="people_meta"
        verbose_name="Phone Type"
        verbose_name_plural="Phone Types"

class EmailContactType(models.Model):
    contact_type = models.TextField(verbose_name='Type')
    display_order = models.IntegerField(default=100)

    def __str__(self):
        return self.contact_type

    class Meta:
        ordering = ['display_order']
        app_label="people_meta"
        verbose_name="Email Type"
        verbose_name_plural="Email Types"

class PhoneNumber(ContactMethod):
    number = models.TextField(verbose_name='Phone Number', null=True, blank=True, default=None)
    contact_type = models.ForeignKey(PhoneContactType, models.SET_NULL, null=True, blank=True, default=None)

    def __str__(self):
        return self.number

    class Meta:
        app_label="people_meta"
        verbose_name="Phone Number"
        verbose_name_plural="Phone Numbers"

class EmailAddress(ContactMethod):
    email = models.TextField(verbose_name='Email Address', null=True, blank=True, default=None)
    contact_type = models.ForeignKey(EmailContactType, models.SET_NULL, null=True, blank=True, default=None)

    def __str__(self):
        return self.email

    class Meta:
        app_label="people_meta"
        verbose_name="Email Address"
        verbose_name_plural="Email Addresses"
