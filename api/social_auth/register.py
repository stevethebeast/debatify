from django.contrib.auth import authenticate
from api.models import User
import os, random, string
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token
from django.conf import settings

def register_social_user(provider, email):
    filtered_user_by_email = User.objects.filter(email=email)
    if filtered_user_by_email.exists() is True:
        if provider == filtered_user_by_email[0].provider:
            registered_user = authenticate(
                email=email, password=settings.SOCIAL_SECRET)
            token, created = Token.objects.get_or_create(user=registered_user)
            return {
                'email': registered_user.email,
                'tokens': token.key}
        else:
            raise AuthenticationFailed(
                detail='Please continue your login using ' + filtered_user_by_email[0].provider)
    else:
        user = {
            'email': email,
            'password': settings.SOCIAL_SECRET, 'mail_confirmed': True, 'provider': provider}
        user = User.objects.create_user(**user)
        new_user = authenticate(
            email=email, password=settings.SOCIAL_SECRET)
        token, created = Token.objects.get_or_create(user=new_user)
        return {
            'email': new_user.email,
            'tokens': token.key
        }
