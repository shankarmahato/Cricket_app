from django.shortcuts import render,get_object_or_404 
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status
from .models import *
from .serializers import *

class TeamView(generics.ListCreateAPIView):
    '''
    list of all teams and create API
    '''
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamDetailView(APIView):
    '''
    Retrieve a particular team data, update and delete it
    '''

    def get_object(self, pk):

        try:
            return Team.objects.get(id=pk)
        except Team.DoesNotExist:
            raise Http404

    def get(self, request,pk,format=None):
        '''
        retreive a team data
        '''
        queryset = self.get_object(pk)

        serializer = TeamPlayerSerializer(queryset)

        return Response(serializer.data)
    
    def put(self, request,pk,format=None):
        '''
        update a existing team data
        '''
        queryset = self.get_object(pk)
        serializer = TeamSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        '''
        delete any existing data
        '''
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PlayerListCreateView(generics.ListCreateAPIView):
    '''
    Create and List all the players
    '''
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayerDetailView(generics.RetrieveUpdateDestroyAPIView):
    '''
    Retrive, Update and Delete any player from the Database
    '''
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class MatchScheduleView(generics.ListCreateAPIView):
    '''
    Automatically generates Fixtures
    '''
    queryset = Matches.objects.all()
    serializer_class = MatchesSerializer

class MatchResultView(generics.ListCreateAPIView):
    '''
    Match Result table
    '''
    queryset = MatchResult.objects.all()
    serializer_class = MatchResultSerializer

class PointsTableView(generics.ListCreateAPIView):
    '''
    Results Table
    '''
    queryset = PointsTable.objects.all()
    serializer_class = PointsTableSerializer

class PlayerStatsView(generics.ListCreateAPIView):
    '''
    Although this section will be automatically but for now you can get and create it from here
    '''
    queryset = PlayerStats.objects.all()
    serializer_class = PlayerStatsSerializer

class PlayerStatsDetailView(generics.RetrieveUpdateDestroyAPIView):
    '''
    Retrive, Update and Delete any PlayerStats from the Database
    '''
    queryset = PlayerStats.objects.all()
    serializer_class = PlayerStatsSerializer


