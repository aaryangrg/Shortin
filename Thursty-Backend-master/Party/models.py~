from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Party(models.Model):   
    #Unique Party identifier
    partyid = models.CharField(max_length = 100, blank = False, null = False, unique = True, primary_key = True)

    #Basic Details
    createdAt = models.DateTimeField(auto_now_add = True)
    eventName = models.CharField(max_length = 100, blank = False, default = "Thursty Party")
    hostedBy = models.CharField(max_length = 100, blank = False)
    hostedByNameCache = models.CharField(max_length = 100, blank = False) #Put organization name here
    time = models.DateTimeField(null = False)
    location = models.CharField(max_length = 100, blank = False, null = False)
    
    #Guest List - indices correspond across these fields to indicate one guest instance 
    guests = ArrayField(models.CharField(blank = True, max_length = 100)) #Indicate User's unique ID here
    guestsNameCache = ArrayField(models.CharField(blank = True, max_length = 200)) #Indicate User's name here
    entryTime = ArrayField(models.DateTimeField(blank = True))
    exitTime = ArrayField(models.DateTimeField(blank = True))
    paymentMethod = ArrayField(models.CharField(default = "Cash", max_length = 50, blank = True))
    
    #Status
    status = models.CharField(max_length = 20, blank = False, default = "Upcoming",)

    class Meta:
        ordering = ('time',)
