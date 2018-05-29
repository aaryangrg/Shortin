#-----------------------
# Purpose: all views associated with organizer's side of the app
# Author: Siddharth Joshi
# Date Created: 04/18/18
#------------------------
from User.models import User, Operator, Organizer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
 
from User.serializers import UserSerializer, OperatorSerializer, OrganizerSerializer

#User API Views
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
 
    def perform_create(self, serializer):
        serializer.save()
 
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    lookup_field = 'uniqueID'
    
    def get_queryset(self):
        queryset = User.objects.all()
        uniqueid = self.kwargs['uniqueID']
        
        if uniqueid is not None:
            queryset = queryset.filter(uniqueID = uniqueid)
        
        return queryset

class UserCollege(generics.ListAPIView):
    serializer_class = UserSerializer
    lookup_field = 'college'

    def get_queryset(self):
        queryset = User.objects.all()
        collegeName = self.kwargs['college']

        if collegeName is not None:
            queryset = queryset.filter(college = collegeName)

        return queryset

#Operator API Views
class OperatorList(generics.ListCreateAPIView):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OperatorDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OperatorSerializer

    def get_queryset(self):
        return Operator.objects.all().filter(user=self.request.user)

#Organizer API View
class OrganizerList(generics.ListCreateAPIView):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrganizerDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrganizerSerializer

    def get_queryset(self):
        return Organizer.objects.all().filter(user=self.request.user)
