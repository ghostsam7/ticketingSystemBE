from __future__ import unicode_literals

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=40, blank = False)
    email = models.EmailField(max_length=254, blank=False)
    contact = PhoneNumberField()

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
