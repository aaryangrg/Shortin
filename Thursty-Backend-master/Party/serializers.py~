from rest_framework import serializers
from Party.models import Party
 
class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ('partyid', 'createdAt', 'eventName', 'hostedBy', 'status', 'time', 'location', 'guests', 'guestsNameCache', 'entryTime', 'exitTime', 'paymentMethod')


