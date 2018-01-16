from django.db import models

# Create your models here.
class ReportedHours(models.Model):
    from people.models import Person
    from projects.models import Role
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
        verbose_name = 'Reported Hours'
        verbose_name_plural = 'Reported Hours'
