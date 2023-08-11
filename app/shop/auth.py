from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from shop.utils import verify_token
import jwt
from rest_framework.response import Response
from rest_framework import status

class CustomJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = self.get_token_from_request(request)
        if not token:
            return None

        try:
            payload = verify_token(token)
            # You might want to return a custom user object or data extracted from the token
            return (None, payload)
        except AuthenticationFailed as e:
            raise e

    def get_token_from_request(self, request):
        authorization_header = request.META.get('HTTP_AUTHORIZATION')
        if authorization_header and authorization_header.startswith('Bearer '):
            return authorization_header.split(' ')[1]
        return None
