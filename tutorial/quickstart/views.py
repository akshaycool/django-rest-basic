from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer,GroupSerializer

class UserViewSet(viewsets.ModelViewSet):

    ''' API to view or edit the list of userss'''
    queryset = User.objects.all().order_by('date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):

    '''API to view or edit groups'''
    queryset= Group.objects.all()
    serializer_class=GroupSerializer







