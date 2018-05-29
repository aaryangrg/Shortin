from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class User(models.Model):
    #Unique Account Identifiers
    uniqueID = models.CharField(null = False, blank = False, max_length = 30, unique = True, primary_key = True)
    universityID = models.CharField(default = "ERROR: no UID", blank = False, max_length = 20)    

    #Basic Information
    firstName = models.CharField(null = False, max_length = 50)
    lastName = models.CharField(null = False, max_length = 50)
    college = models.CharField(default = "UCLA", max_length = 100)

    #Contact Information 
    email = models.CharField(null = False, max_length = 100)
    phone = models.CharField(default = "N/A", max_length = 20)

    #Account Type
    isOperator = models.BooleanField(default = False)
    isOrganizer = models.BooleanField(default = False)
    
    #Party-goer fields - these fields store the partyid
    goingTo = ArrayField(models.CharField(max_length = 100, blank = True))
    attendedParties = ArrayField(models.CharField(max_length = 100, blank = True))
    
    #Party-goer cache fields
    goingToNameCache = ArrayField(models.CharField(max_length = 100, blank = True))
    attendedPartiesNameCache = ArrayField(models.CharField(max_length = 100, blank = True))
    attendedPartiesEntryCache = ArrayField(models.DateTimeField(blank = True))
    attendedPartiesExitCache = ArrayField(models.DateTimeField (blank = True))

class Operator(models.Model):
    #OneToOne mapping to User
    user = models.CharField(max_length = 100, blank = False, unique = True, primary_key = True) #contains the user uniqueID
    
    #Parties that the operator has checkIn priveleges for - this fields stores the partyid
    checkInPermissionsFor = ArrayField(models.CharField(max_length = 100, blank = True))
    
    #Party Cache Fields
    checkInPermissionsForNameCache = ArrayField(models.CharField(max_length = 100, blank = True))

class Organizer(models.Model):
    #OneToOne mapping to User
    user = models.CharField(max_length = 100, blank = False, unique = True, primary_key = True) #contains the user uniqueID
    
    #Name of Organization that organizer hosts parties for
    organizationName = models.CharField(max_length = 100, blank = False)
    collegeName = models.CharField(max_length = 100, blank = True, default = "UCLA")
    
    #Parties that are associated with this organizer - this field stores the partyid
    pastParties = ArrayField(models.CharField(max_length = 100, blank = True))
    currentParties = ArrayField(models.CharField(max_length = 100, blank = True))
    upcomingParties = ArrayField(models.CharField(max_length = 100, blank = True))

    #Party Cache Fields
    pastPartiesNameCache = ArrayField(models.CharField(max_length = 100, blank = True))
    currentPartiesNameCache = ArrayField(models.CharField(max_length = 100, blank = True))
    upcomingPartiesNameCache = ArrayField(models.CharField(max_length = 100, blank = True))


