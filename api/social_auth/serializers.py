import os, sys
from rest_framework import serializers
from .register import register_social_user
from . import google, facebook, twitterhelper
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings


class FacebookSocialAuthSerializer(serializers.Serializer):
    """Handles serialization of facebook related data"""
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = facebook.Facebook.validate(auth_token)
        try:
            email = user_data['email']
            provider = 'facebook'
            return register_social_user(
                provider=provider,
                email=email
        )
        except Exception as identifier:

            raise serializers.ValidationError(
                'The token  is invalid or expired. Please login again.'
            )


class GoogleSocialAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = google.Google.validate(auth_token)
        #try:
        #user_data['sub']
        sys.stderr.write("GOOGLE SUB " + user_data['sub'])
        sys.stderr.write("GOOGLE AUD " + user_data['aud'])
        #except:
        #    raise serializers.ValidationError(
        #        'The token is invalid or expired. Please login again.'
        #    )
        #if user_data['aud'] != settings.GOOGLE_CLIENT_ID:
        #    raise AuthenticationFailed('oops, who are you?')
        email = user_data['email']
        provider = 'google'
        return register_social_user(
            provider=provider, email=email)


class TwitterAuthSerializer(serializers.Serializer):
    """Handles serialization of twitter related data"""
    access_token_key = serializers.CharField()
    access_token_secret = serializers.CharField()

    def validate(self, attrs):
        access_token_key = attrs.get('access_token_key')
        access_token_secret = attrs.get('access_token_secret')
        user_info = twitterhelper.TwitterAuthTokenVerification.validate_twitter_auth_tokens(
            access_token_key, access_token_secret)
        try:
            user_id = user_info['id_str']
            email = user_info['email']
            name = user_info['name']
            provider = 'twitter'
        except:
            raise serializers.ValidationError(
                'The tokens are invalid or expired. Please login again.'
            )
        return register_social_user(
            provider=provider, user_id=user_id, email=email, name=name)
