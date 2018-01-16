from django.db import models

# Create your models here.
class FundingType(models.Model):
    name = models.TextField()
    display_order = models.IntegerField(default=100)
    notes = models.TextField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['display_order', 'name']
        verbose_name = 'Funding Type'
        verbose_name_plural = 'Funding Types'

class Funding(models.Model):
    from people.models import Organization
    organization = models.ForeignKey(Organization, models.SET_NULL, null=True, blank=True, default=None)
    name = models.TextField(null=True, blank=True, default=None)
    amount = models.FloatField(null=True, blank=True, default=None)
    start_date = models.DateField(null=True, blank=True, default=None)
    end_date = models.DateField(null=True, blank=True, default=None)
    funding_type = models.ForeignKey(FundingType, models.SET_NULL, verbose_name="Type", null=True, blank=True, default=None)
    probability = models.IntegerField(default=50, verbose_name="Probability of Funding")
    billing_code = models.TextField(null=True, blank=True, default=None)
    notes = models.TextField(null=True, blank=True, default=None)

    def __str__(self):
        if self.name:
            return "%s - %s" % (self.name, self.billing_code)
        else:
            return "%s - %s" % (self.organization, self.billing_code)

    class Meta:
        ordering = ['start_date', 'end_date', 'name', 'organization']
        verbose_name = 'Funding'
        verbose_name_plural = 'Fundings'


class Task(models.Model):
    from projects.models import Milestone
    code = models.TextField(verbose_name="Task Code")
    milestone = models.ForeignKey(Milestone, models.SET_NULL, null=True, blank=True, default=None)
    funding = models.ForeignKey(Funding, models.SET_NULL, null=True, blank=True, default=None)
    start_date = models.DateField(null=True, blank=True, default=None)
    end_date = models.DateField(null=True, blank=True, default=None)
    budget = models.FloatField(null=True, blank=True, default=None)
    notes = models.TextField(null=True, blank=True, default=None)

    def __str__(self):
        if self.milestone:
            return "%s: %s" % (self.milestone, self.code)
        else:
            return self.code

    class Meta:
        ordering = ['code']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
