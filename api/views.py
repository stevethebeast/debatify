from django.shortcuts import render
import sys

# Create your views here.
from rest_framework import viewsets, views, status, filters, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import render
from django.db.models import F
from django.db import connection
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from .serializers import DebateSerializer, ArgumentSerializer,\
CounterArgumentSerializer, DebateVoteSerializer, ArgumentVoteSerializer, CounterArgumentVoteSerializer, VotingRightSerializer, DebateArgumentsSerializer,\
GetCounterArgumentByArgumentIDSerializer, GetTokenUsernameSerializer
from .models import Debate, Argument, Counter_argument, Debate_vote, Argument_vote,\
Counter_argument_vote, Voting_right

#class ContactViewSet(viewsets.ModelViewSet):
#    permission_classes = [IsAuthenticatedOrReadOnly]
#    queryset = Contact.objects.all().order_by('ID')
#    serializer_class = ContactSerializer

class DebateViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Debate.objects.all().order_by('ID')
    serializer_class = DebateSerializer

class ArgumentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Argument.objects.all().order_by('ID')
    serializer_class = ArgumentSerializer

class CounterArgumentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Counter_argument.objects.all().order_by('ID')
    serializer_class = CounterArgumentSerializer

class DebateVoteViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Debate_vote.objects.all().order_by('ID')
    serializer_class = DebateVoteSerializer

class ArgumentVoteViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Argument_vote.objects.all().order_by('ID')
    serializer_class = ArgumentVoteSerializer

class CounterArgumentVoteViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Counter_argument_vote.objects.all().order_by('ID')
    serializer_class = CounterArgumentVoteSerializer

class VotingRightViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Voting_right.objects.all().order_by('DEBATE_ID')
    serializer_class = VotingRightSerializer

class SearchDebatesAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ['NAME', 'YES_TITLE', 'NO_TITLE']
    filter_backends = (filters.SearchFilter,)
    queryset = Debate.objects.all()
    serializer_class = DebateSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def ListOfArguments(request):
    if request.method == 'GET':
        #user = Token.objects.get(key=request.auth.key).user_id
        sys.stderr.write("yolo " +str(user))
        debateid = request.query_params.get('id', None)
        side = request.query_params.get('side', None)
        if debateid and side is None:
            arguments = Argument.objects.annotate(Username=F('CONTACT_ID__email')).values('SIDE','ID','TITLE','TEXT','SCORE','Username')
        elif debateid is None:
            arguments = Argument.objects.filter(DEBATE_ID=debateid).annotate(Username=F('CONTACT_ID__email')).values('SIDE','ID','TITLE','TEXT','SCORE','Username')
        elif side is None:
            arguments = Argument.objects.filter(SIDE=side).annotate(Username=F('CONTACT_ID__email')).values('SIDE','ID','TITLE','TEXT','SCORE','Username')
        else:
            arguments = Argument.objects.all().annotate(Username=F('CONTACT_ID__email')).values('SIDE','ID','TITLE','TEXT','SCORE','Username')
        #♣sys.stderr.write(arguments)
        arguments_serializer = DebateArgumentsSerializer(arguments, many=True)
        return Response(arguments_serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
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

@api_view(['GET','POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def GetOrCreateUser(request):
    if request.method == 'GET':
        argumentid = request.query_params.get('id', None)
        if argumentid is None:
            content = {"Bad request": "Please put an id as argument"}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        else:
            counterarguments = Counter_argument.objects.filter(ARGUMENT_ID=argumentid).annotate(Username=F('CONTACT_ID__NAME')).values('ID','TITLE','TEXT','SCORE','Username')
        counterarguments_serializer = GetCounterArgumentByArgumentIDSerializer(counterarguments, many=True)
        return Response(counterarguments_serializer.data)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def GetOrCreateDebateVote(request):
    key=request.auth
    user = None
    debatevote = None
    if key is not None:
        user = Token.objects.get(key=key).user_id
    #sys.stderr.write("yolo " +str(user))
    if request.method == 'GET':
        debateid = request.query_params.get('id', None)
        if debateid is None:
            content = {"Bad request": "Please put an id as argument"}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        if user is not None:
            debatevote = Debate_vote.objects.filter(DEBATE_ID=debateid, CONTACT_ID=user).all()
        else:
            debatevote = Debate_vote.objects.all().order_by('DEBATE_ID')
        if debatevote is not None:
            serializer = DebateVoteSerializer(debatevote, many=True)
            return Response(serializer.data)
        else:
            return Response({"Response":"Nothing to see here"})
    else:
        data = JSONParser().parse(request)
        serializer = DebateVoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.errors, status=400)

@api_view(['GET'])
#@permission_classes([IsAuthenticatedOrReadOnly])
def ListDebatesWithUserChoices(request):
    key=request.auth
    user = None
    if key is not None:
        user = Token.objects.get(key=key).user_id
        return Response(Debate.objects.with_debatevotes(debateid, user))
    else:
        content = Debate.objects.all().order_by('ID')
        serializer = DebateSerializer(content, many=True)
        return Response(serializer.data)

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def ListCounterArgumentsWithUserChoices(request):
    key=request.auth
    user = None
    argumentid = request.query_params.get('id', None)
    if argumentid is None:
        content = {"Bad request": "Please put an id as argument"}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
    if key is not None:
        user = Token.objects.get(key=key).user_id
        return Response(Counter_argument.objects.with_userchoices(argumentid, user))
    else:
        content = Counter_argument.objects.all().order_by('ID')
        serializer = ArgumentSerializer(content, many=True)
        return Response(serializer.data)

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def ListArgumentsWithUserChoices(request):
    key=request.auth
    user = None
    debateid = request.query_params.get('id', None)
    if debateid is None:
        content = {"Bad request": "Please put an id as argument"}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
    if key is not None:
        user = Token.objects.get(key=key).user_id
        return Response(Argument.objects.with_debateargumentlikes(debateid, user))
    else:
        content = Argument.objects.all().order_by('ID')
        serializer = ArgumentSerializer(content, many=True)
        return Response(serializer.data)

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def GetAllCounterArgumentsWithLikesByArgumentID(request):
    key=request.auth
    user = None
    counterargumentid = request.query_params.get('id', None)
    if counterargumentid is None:
        content = {"Bad request": "Please put an id as argument"}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
    if key is not None:
        user = Token.objects.get(key=key).user_id
        return Response(Counter_argument.objects.with_counterargumentlikes(counterargumentid, user))
    else:
        content = Argument.objects.all().order_by('ID')
        serializer = CounterArgumentSerializer(content, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetTokenUsername(request):
    key = request.auth
    if key is not None:
        return Response({#"Email": request.user.email,\
        "NAME": request.user.first_name + " " + request.user.last_name#, "Last name": request.user.last_name\
        })