import jwt
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed

def get_object_or_none(model, *args, **kwargs):
    try:
        return model.objects.get(*args, **kwargs)
    except model.DoesNotExist:
        return None
    
def verify_token(token):
    try:
        # Verify the JWT token
        decoded_token = jwt.decode(
            token, settings.SECRET_KEY, algorithms=['HS256'])

        return decoded_token

    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed(detail={"error":"Token expired", "code": 401})
    except jwt.InvalidTokenError:
        raise AuthenticationFailed(detail={"error":"Token invalid", "code": 400})
