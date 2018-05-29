#-----------------------
# Purpose: Stores all urls associated with user, operator and organizer side of the app
# Author: Siddharth Joshi
# Date Created: 05/08/18
#------------------------                                                                                                                                                                                  
from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns
from User import views

urlpatterns = [
   #Regular User urls
   re_path(r'all/$', views.UserList.as_view(), name='user-list'),
   re_path(r'search/(?P<id>)/$', views.UserDetail.as_view(), name='user-detail'),
   re_path(r'filter/college/(?P<college>)/$', views.UserCollege.as_view(), name='user-college-detail'),
   
   #Operator urls
   re_path(r'all/operator/$', views.OperatorList.as_view(), name='operator-list'),
   re_path(r'operator/search/(?P<id>)/$', views.OperatorDetail.as_view(), name='operator-detail'),
   re_path(r'operator/filter/college/(?P<college>)/$', views.OperatorCollege.as_view(), name='operator-college-detail'),
   
   #Organizer urls
   re_path(r'organizer/all/$', views.OrganizerList.as_view(), name='organizer-list'),
   re_path(r'organizer/search/(?P<id>)/$', views.OrganizerDetail.as_view(), name='organizer-detail'),
   re_path(r'organizer/filter/college/(?P<college>)/$', views.OrganizerCollege.as_view(), name='organizer-college-detail'),
]
