# Get self user data, available for authenticated User
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from kiddie_closet_app.serializers.users import RegisterSerializer, UserSerializer


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