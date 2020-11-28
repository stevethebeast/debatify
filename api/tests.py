from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate, APITestCase, APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import User, Debate, Argument
import sys


class APItests(APITestCase):
    def setUp(self):
        User.objects.create_superuser('JesusChrist@gmail.com', 'IlikeTrains69')
        Debate.objects.create(NAME='Legalize Marihuana', YES_TITLE='It\'s good', NO_TITLE='It\'s dangerous', CONTEXT='We live in a very boring society')
        debate = Debate.objects.get(NAME='Legalize Marihuana')
        user = User.objects.get(email='JesusChrist@gmail.com')
        Argument.objects.create(TITLE='No, la marihuana esta mal', TEXT='ay marica la marihuana est mal porque Pablito ha fumado un porlo y le dolio el estromago', DEBATE_ID=debate, CONTACT_ID=user, SIDE='NO')
        #User.objects.create_user('leidivelazquez@colombiamail.co', '19071969', first_name='Leidi', last_name='Velazquez')

    def test_login(self):
        client = APIClient()
        response = client.post('/api/auth/token/login/', {"email": "JesusChrist@gmail.com","password": "IlikeTrains69"}, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_failed(self):
        client = APIClient()
        response = client.post('/api/auth/token/login/', {"email": "JesusChrist@gmail.com","password": "IlikeTrainfgfgs69"}, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_creation(self):
        user = User.objects.get(email='JesusChrist@gmail.com')
        token = Token.objects.create(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.post('/api/auth/users/', {"email": "leidivelazquez@colombiamail.co", "password":"19071969fecha", "first_name":"Leidi", "last_name":"Velazquez"}, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_listdebatewithuserchoices_withouttoken(self):
        client = APIClient()
        response = client.get('/ListDebatesWithUserChoices')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_listdebatewithuserchoices_withtoken(self):
        user = User.objects.get(email='JesusChrist@gmail.com')
        token = Token.objects.create(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get('/ListDebatesWithUserChoices')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_listargumentswithuserchoices_withouttoken_noparamerror(self):
        client = APIClient()
        response = client.get('/ListArgumentsWithUserChoices')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_listargumentswithuserchoices_withtoken_noparamerror(self):
        user = User.objects.get(email='JesusChrist@gmail.com')
        token = Token.objects.create(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get('/ListArgumentsWithUserChoices')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_listcounterargumentswithuserchoices_withouttoken_noparamerror(self):
        client = APIClient()
        response = client.get('/ListCounterArgumentsWithUserChoices')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_listcounterargumentswithuserchoices_withtoken_noparamerror(self):
        user = User.objects.get(email='JesusChrist@gmail.com')
        token = Token.objects.create(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get('/ListCounterArgumentsWithUserChoices')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_listargumentswithuserchoices_withouttoken(self):
        client = APIClient()
        response = client.get('/ListArgumentsWithUserChoices?id=1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_listargumentswithuserchoices_withtoken(self):
        user = User.objects.get(email='JesusChrist@gmail.com')
        token = Token.objects.create(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get('/ListArgumentsWithUserChoices?id=1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_listcounterargumentswithuserchoices_withouttoken(self):
        client = APIClient()
        response = client.get('/ListCounterArgumentsWithUserChoices?id=1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_listcounterargumentswithuserchoices_withtoken(self):
        user = User.objects.get(email='JesusChrist@gmail.com')
        token = Token.objects.create(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get('/ListCounterArgumentsWithUserChoices?id=1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getTokenUsername(self):
        user = User.objects.get(email='JesusChrist@gmail.com')
        token = Token.objects.create(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get('/GetTokenUsername')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getTokenUsername_errornotoken(self):
        client = APIClient()
        response = client.get('/GetTokenUsername')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)