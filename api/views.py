from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, views, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.db.models import F
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import ContactSerializer, DebateSerializer, ArgumentSerializer,\
CounterArgumentSerializer, DebateVoteSerializer, ArgumentVoteSerializer, CounterArgumentVoteSerializer, VotingRightSerializer
#, DebateArgumentsSerializer
from .models import Contact, Debate, Argument, Counter_argument, Debate_vote, Argument_vote,\
Counter_argument_vote, Voting_right

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('ID')
    serializer_class = ContactSerializer

class DebateViewSet(viewsets.ModelViewSet):
    queryset = Debate.objects.all().order_by('ID')
    serializer_class = DebateSerializer

class ArgumentViewSet(viewsets.ModelViewSet):
    queryset = Argument.objects.all().order_by('ID')
    serializer_class = ArgumentSerializer

class CounterArgumentViewSet(viewsets.ModelViewSet):
    queryset = Counter_argument.objects.all().order_by('ID')
    serializer_class = CounterArgumentSerializer

class DebateVoteViewSet(viewsets.ModelViewSet):
    queryset = Debate_vote.objects.all().order_by('ID')
    serializer_class = DebateVoteSerializer

class ArgumentVoteViewSet(viewsets.ModelViewSet):
    queryset = Argument_vote.objects.all().order_by('ID')
    serializer_class = ArgumentVoteSerializer

class CounterArgumentVoteViewSet(viewsets.ModelViewSet):
    queryset = Counter_argument_vote.objects.all().order_by('ID')
    serializer_class = CounterArgumentVoteSerializer

class VotingRightViewSet(viewsets.ModelViewSet):
    queryset = Voting_right.objects.all().order_by('DEBATE_ID')
    serializer_class = VotingRightSerializer