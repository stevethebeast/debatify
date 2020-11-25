from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate, APITestCase, APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import User
import sys


class APItests(APITestCase):
    def setUp(self):
        User.objects.create_superuser('JesusChrist@gmail.com', 'IlikeTrains69')
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
