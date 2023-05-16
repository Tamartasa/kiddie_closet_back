# Get self user data, available for authenticated User
import jwt
import requests
from django.contrib.auth.models import User
from google.oauth2 import id_token
from google.auth.transport import requests
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from kiddie_closet_app.serializers.users import RegisterSerializer, UserSerializer

@api_view(['POST'])
def google_auth(request):
    CLIENT_ID = "777826670126-d4jtjnif246030bhcuouh35ptrphtcik.apps.googleusercontent.com"
    google_token = request.headers['Authorization']
    print('auth header', google_token)
    idinfo = id_token.verify_oauth2_token(google_token, requests.Request(), CLIENT_ID)
    # res = jwt.decode(jwt=google_token, algorithms=["RS256"], key="")
    print(idinfo)
    # Process the ID token
    # Assuming authentication is successful, return a response
    return Response({"message": "Authentication successful"})

# signup as user (available for all) or staff (available only by staff user)
@api_view(['POST'])
def sign_up(request):
    serializer = RegisterSerializer(data=request.data, many=False, context={'request': request})
    if serializer.is_valid(raise_exception=True):
        new_user = serializer.create(serializer.validated_data)
        print(Response)
        return Response(data=UserSerializer(instance=new_user, many=False).data)


# Get all current user's data - available only for logged-in users
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_user_data(request):
        serializer = UserSerializer(instance=request.user, many=False)
        return Response(serializer.data)


# Get all users data or search by name, available for User.is_staff = True
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def get_all_users(request):
    users_qs = User.objects.all()

    if 'name' in request.query_params:
        users_qs = users_qs.filter(first_name__icontains=request.query_params['name']) or users_qs.filter(last_name__icontains=request.query_params['name'])

    serializer = UserSerializer(users_qs, many=True)
    if not serializer.data:
        return Response(data=[], status=status.HTTP_204_NO_CONTENT)

    return Response(serializer.data)