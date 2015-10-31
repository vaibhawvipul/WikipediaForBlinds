from django.db import models
from django.contrib.auth.models import User
import os

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    Institution = models.CharField(max_length=128,blank=False)
    City = models.CharField(max_length=128,blank=True)
    Country = models.CharField(max_length=128,blank=False)

    def __unicode__(self):
        return self.user.username
