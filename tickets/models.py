from __future__ import unicode_literals

from django.db import models
from customers.models import Customer
from staffs.models import Staff

# Create your models here.
status_choice = (
    ('o','open'),
    ('c','closed'),
    ('a','assigned'),
)

class Ticket(models.Model):
    title = models.CharField(max_length = 80, blank = False)
    description = models.TextField(blank = False)
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE)
    staff = models.ForeignKey('staffs.Staff', on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length = 8, choices=status_choice, default = 'o')
    resolved = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
