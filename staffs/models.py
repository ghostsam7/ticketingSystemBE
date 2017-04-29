from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=40, blank = False)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
