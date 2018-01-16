from django.db import models

# Create your models here.
class Project(models.Model):
    from people.models import Organization
    name = models.TextField(verbose_name='Project Name')
    start_date = models.DateField(null=True, blank=True, default=None)
    end_date = models.DateField(null=True, blank=True, default=None)
    probability = models.IntegerField(verbose_name='Probability of Project', default=50)
    organization = models.ForeignKey(Organization, models.SET_NULL, verbose_name='Client Organization', null=True, blank=True, default=None)
    notes = models.TextField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['start_date', 'end_date']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

class MilestoneType(models.Model):
    milestone_type = models.TextField()
    display_order = models.IntegerField(default=100)

    def __str__(self):
        return self.milestone_type

    class Meta:
        ordering = ['display_order', 'milestone_type']
        verbose_name = 'Milestone Type'
        verbose_name_plural = 'Milestone Types'

class Milestone(models.Model):
    name = models.TextField()
    milestone_type = models.ForeignKey(MilestoneType, models.SET_NULL, null=True, blank=True, default=None)
    start_date = models.DateField(null=True, blank=True, default=None)
    end_date = models.DateField(null=True, blank=True, default=None)
    # Attempting to implement this: https://stackoverflow.com/questions/39859224/how-to-use-html5-color-picker-in-django-admin
    color = models.CharField(max_length=7)
    description = models.TextField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['start_date', 'end_date', 'name']
        verbose_name = 'Milestone'
        verbose_name_plural = 'Milestones'

class Role(models.Model):
    name = models.TextField()
    project = models.ForeignKey(Project, models.CASCADE)
    billing_rate = models.FloatField(null=True, blank=True, default=None)
    budgeted_hours = models.FloatField(default=0.0)
    notes = models.TextField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

class Assignment(models.Model):
    from people.models import Person
    person = models.ForeignKey(Person, models.CASCADE)
    role = models.ForeignKey(Role, models.CASCADE)
    notes = models.TextField(null=True, blank=True, default=None)

    def __str__(self):
        return "%s: %s" % (self.role, self.person)

    class Meta:
        ordering = ['role', 'person']
        verbose_name = 'Assignment'
        verbose_name_plural = 'Assignments'

class ProposedHours(models.Model):
    from people.models import Person
    from funding.models import Task
    person = models.ForeignKey(Person, models.CASCADE, null=True, blank=True, default=None)
    role = models.ForeignKey(Role, models.CASCADE)
    hours = models.FloatField()
    date = models.DateField()
    task = models.ForeignKey(Task, models.SET_NULL, null=True, blank=True, default = None)
    notes = models.TextField(null=True, blank=True, default = None)

    def __str__(self):
        return "%s: %s, %s" % (str(self.date), self.person, str(self.hours))

    class Meta:
        ordering = ['date', 'role', 'person', 'hours']
        verbose_name = 'Proposed Hours'
        verbose_name_plural = 'Proposed Hours'
