from rest_framework import serializers
from User.models import User, Operator, Organizer
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('uniqueID', 'universityID', 'firstName', 'lastName', 'college', 'email', 'phone', 'isOperator', 'isOrganizer', 'goingTo', 'attendedParties', 'goingToNameCache', 'attendedPartiesNameCache', 'attendedPartiesEntryCache', 'attendedPartiesExitCache')

class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operator
        fields = ('user', 'currentParties', 'upcomingParties', 'pastParties', 'currentPartiesNameCache', 'upcomingPartiesNameCache', 'pastPartiesNameCache')
        
class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        fields = ('user', 'organizationName', 'collegeName', 'currentPartiesNameCache', 'upcomingPartiesNameCache', 'pastPartiesNameCache', 'currentParties', 'upcomingParties', 'pastParties') 
