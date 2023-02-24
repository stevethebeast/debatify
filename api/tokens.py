from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework.permissions import BasePermission
from django.conf import settings
from django.urls import re_path
from djoser.urls import authtoken
from djoser import views
import six

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )
account_activation_token = TokenGenerator()

class SafelistPermission(BasePermission):
    """
    Ensure the request's IP address is on the safe list configured in Django settings.
    """
    def has_permission(self, request, view):
        remote_addr = request.META['REMOTE_ADDR']
        for valid_ip in settings.REST_SAFE_LIST_IPS:
            if remote_addr == valid_ip or remote_addr.startswith(valid_ip) or valid_ip == 'ALLOW_ALL':
                return True
        return False