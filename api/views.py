# SITE KEY 6LczFhIaAAAAAARMWCYvEN5-lREWVVBX0J8N4aFU
# SECRET KEY 6LczFhIaAAAAAIVGoowshcsphaMMS1N_wh1JfvSS
from django.shortcuts import render
import sys, requests, json, urllib.request

# Create your views here.
from rest_framework import viewsets, views, status, filters, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import render
from django.db.models import F, Count
from django.db.models.functions import Cast
from django.db import connection, models
from django.core.mail import send_mail
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from .serializers import DebateSerializer, ArgumentSerializer,\
CounterArgumentSerializer, DebateVoteSerializer, ArgumentVoteSerializer, CounterArgumentVoteSerializer, DebateArgumentsSerializer,\
GetCounterArgumentByArgumentIDSerializer, GetTokenUsernameSerializer, CategorySerializer, UserSerializer
from .models import Debate, Argument, Counter_argument, Debate_vote, Argument_vote,\
Counter_argument_vote, Category, User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.conf import settings
from django.template import loader
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

class DebateViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Debate.objects.all().order_by('ID')
    serializer_class = DebateSerializer

    def create(self, request):
        key=request.auth
        user=Token.objects.get(key=key).user_id
        data = JSONParser().parse(request)
        data['CREATOR_ID'] = user
        serializer = DebateSerializer(data=data)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.errors, status=400)

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all().order_by('ID')
    serializer_class = CategorySerializer

class ArgumentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Argument.objects.all().order_by('ID')
    serializer_class = ArgumentSerializer

    def create(self, request):
        key=request.auth
        user=Token.objects.get(key=key).user_id
        data = JSONParser().parse(request)
        data['CONTACT_ID'] = user
        serializer = ArgumentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.errors, status=400)

class CounterArgumentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Counter_argument.objects.all().order_by('ID')
    serializer_class = CounterArgumentSerializer

    def create(self, request):
        key=request.auth
        user=Token.objects.get(key=key).user_id
        data = JSONParser().parse(request)
        data['CONTACT_ID'] = user
        serializer = CounterArgumentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.errors, status=400)

class DebateVoteViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Debate_vote.objects.all().order_by('ID')
    serializer_class = DebateVoteSerializer

    def create(self, request):
        key=request.auth
        user=Token.objects.get(key=key).user_id
        data = JSONParser().parse(request)
        data['CONTACT_ID'] = user
        serializer = DebateVoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.errors, status=400)

class ArgumentVoteViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Argument_vote.objects.all().order_by('ID')
    serializer_class = ArgumentVoteSerializer

    def create(self, request):
        key=request.auth
        user=Token.objects.get(key=key).user_id
        data = JSONParser().parse(request)
        data['CONTACT_ID'] = user
        serializer = ArgumentVoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.errors, status=400)

class CounterArgumentVoteViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Counter_argument_vote.objects.all().order_by('ID')
    serializer_class = CounterArgumentVoteSerializer

    def create(self, request):
        key=request.auth
        user=Token.objects.get(key=key).user_id
        data = JSONParser().parse(request)
        data['CONTACT_ID'] = user
        serializer = CounterArgumentVoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.errors, status=400)

class SearchDebatesAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ['NAME', 'YES_TITLE', 'NO_TITLE']
    filter_backends = (filters.SearchFilter,)
    queryset = Debate.objects.filter(IS_PUBLIC=1).all()
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
        return Response(Debate.objects.with_debatevotes(user))
    else:
        content = list(Debate.objects.annotate(FIRST_NAME=F('CREATOR_ID__first_name'),LAST_NAME=F('CREATOR_ID__last_name'),CREATED_AT_STR=Cast('CREATED_AT', output_field=models.CharField())).values('ID','NAME','YES_TITLE','NO_TITLE','CONTEXT','PHOTO_PATH','IS_PUBLIC','FIRST_NAME','LAST_NAME','CREATOR_ID','CATEGORY_ID','CREATED_AT_STR').order_by('ID'))
        return Response(content)

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
        content = list(Counter_argument.objects.annotate(FIRST_NAME=F('CONTACT_ID__first_name'),LAST_NAME=F('CONTACT_ID__last_name'),CREATED_AT_STR=Cast('CREATED_AT', output_field=models.CharField())).values('ID','TITLE','TEXT','ARGUMENT_ID','SCORE','CONTACT_ID','FIRST_NAME','LAST_NAME','CREATED_AT_STR').order_by('ID'))
        return Response(content)

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
        content = list(Argument.objects.annotate(FIRST_NAME=F('CONTACT_ID__first_name'),LAST_NAME=F('CONTACT_ID__last_name'),CREATED_AT_STR=Cast('CREATED_AT', output_field=models.CharField())).values('ID','TITLE','TEXT','DEBATE_ID','SCORE','CONTACT_ID','SIDE','FIRST_NAME','LAST_NAME','CREATED_AT_STR').order_by('ID'))
        return Response(content)

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
        content = Counter_argument.objects.all().order_by('ID')
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

@api_view(['GET'])
#@permission_classes([AllowAny])
def DebateVotesbyDebateId(request):
    debateid = request.query_params.get('id', None)
    if debateid is None:
        content = {"Bad request": "Please put an id as argument"}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
    else:
        yes = Debate_vote.objects.filter(SIDE='yes', DEBATE_ID=debateid).all().aggregate(Count('DEBATE_ID')).values()
        no = Debate_vote.objects.filter(SIDE='no', DEBATE_ID=debateid).all().aggregate(Count('DEBATE_ID')).values()
        return Response({"YES": list(yes)[0], "NO": list(no)[0]}, status= status.HTTP_200_OK,content_type='application/json')

@api_view(['POST'])
#@permission_classes([AllowAny])
def CreateUserWithConfirmation(request):
    data = JSONParser().parse(request)
    response = requests.post(settings.DOMAIN + "/api/auth/users/", data=data)
    #sys.stderr.write("yolo " +str(data))
    #serializer = UserSerializer(data=data)
    if response.raise_for_status() is None:
        resp = response.json()
        createdUser = User.objects.get(email=resp["email"])
        #sys.stderr.write(serializer.data)
        #current_site = get_current_site(request)
        #User.objects.filter(email=createdUser.email).update(is_active=False)
        mail_subject = 'Activate your blog account.'
        message = render_to_string('acc_active_email.html', {
            'user': createdUser.email,
            'domain': settings.DOMAIN,
            'uid':urlsafe_base64_encode(force_bytes(createdUser.id)),
            'token':account_activation_token.make_token(createdUser),
        })
        send_mail(mail_subject, 
            message, settings.EMAIL_HOST_USER, [createdUser.email], fail_silently = False)
        return Response({"Register":"Please confirm your email address to complete the registration"}, status= status.HTTP_200_OK,content_type='application/json')
    else:
        return Response("Error sending mail")

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        #User.objects.filter(pk=uid).update(is_active=True)
        user.mail_confirmed = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        user = authenticate(email=data["email"], password=data["password"])
        if user is not None and user.mail_confirmed is True:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({"Error":"User not yet confirmed"}, status=status.HTTP_423_LOCKED)

def contact(request):
    return render(request, 'contact.html')

@api_view(('POST',))
def recaptcha_valid(request):
    recaptcha_response = request.POST.get('g-recaptcha-response')
    url = 'https://www.google.com/recaptcha/api/siteverify'
    payload = {
        'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        'response': recaptcha_response
    }
    data = urllib.parse.urlencode(payload).encode()
    req = urllib.request.Request(url, data=data)
    response = urllib.request.urlopen(req)
    result = json.loads(response.read().decode())
    if result['success']:
        return Response({"Recaptcha status":"Success"})
    else:
        return Response({"Recaptcha status":"Error"})