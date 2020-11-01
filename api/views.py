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
CounterArgumentSerializer, DebateVoteSerializer, ArgumentVoteSerializer, CounterArgumentVoteSerializer, VotingRightSerializer, DebateArgumentsSerializer,\
GetCounterArgumentByArgumentIDSerializer
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

@api_view(['GET'])
def ListOfArguments(request):
    if request.method == 'GET':
        debateid = request.query_params.get('id', None)
        side = request.query_params.get('side', None)
        if debateid and side is None:
            arguments = Argument.objects.annotate(Username=F('CONTACT_ID__NAME')).values('SIDE','ID','TITLE','TEXT','SCORE','Username')
        elif debateid is None:
            arguments = Argument.objects.filter(DEBATE_ID=debateid).annotate(Username=F('CONTACT_ID__NAME')).values('SIDE','ID','TITLE','TEXT','SCORE','Username')
        elif side is None:
            arguments = Argument.objects.filter(SIDE=side).annotate(Username=F('CONTACT_ID__NAME')).values('SIDE','ID','TITLE','TEXT','SCORE','Username')
        else:
            arguments = Argument.objects.all().annotate(Username=F('CONTACT_ID__NAME')).values('SIDE','ID','TITLE','TEXT','SCORE','Username')
        arguments_serializer = DebateArgumentsSerializer(arguments, many=True)
        return Response(arguments_serializer.data)

@api_view(['GET'])
def ListOfCounterArguments(request):
    if request.method == 'GET':
        argumentid = request.query_params.get('id', None)
        if argumentid is None:
            content = {"Bad request": "Please put an id as argument"}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        else:
            counterarguments = Counter_argument.objects.filter(ARGUMENT_ID=argumentid).annotate(Username=F('CONTACT_ID__NAME')).values('ID','TITLE','TEXT','SCORE','Username')
        counterarguments_serializer = GetCounterArgumentByArgumentIDSerializer(counterarguments, many=True)
        return Response(counterarguments_serializer.data)