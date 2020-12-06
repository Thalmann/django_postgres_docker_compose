from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):

    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Organization(BaseModel):
    name = models.CharField(max_length=100)


class UserProfile(BaseModel):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)


class Monitor(BaseModel):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    interval_in_ms = models.IntegerField()
    protocol = models.CharField(max_length=50)
    server = models.CharField(max_length=200)
    port = models.IntegerField()

    def is_up(self):
        return self.check_set.last().up


class Check(BaseModel):
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)
    up = models.BooleanField()
