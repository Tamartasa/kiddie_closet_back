from rest_framework.viewsets import ModelViewSet

from kiddie_closet_app.models import Ad
from kiddie_closet_app.serializers.ads import AdSerializer

class AdPermissions(BaseException):
    # Get all ads - available for all

    # Add new ad - available for logged-in users
    def has_permission(self, request, view):
        if request.method in ['POST']:
            return request.user.is_authenticated
        return True

    # Update ad - available only for logged-in staff users or
    # non-staff logged-in user that published the ad:
    def has_object_permission(self, request, view, obj):
        if request.method in ['PATCH', 'PUT', 'DELETE']:
            return request.user.is_authenticated and request.user.is_staff or\
                    request.user.is_authenticated and request.user.id == obj.user_id
        return True

class AdsViewSet(ModelViewSet):
    queryset = Ad.objects.all()

    permission_classes = [AdPermissions]

    serializer_class = AdSerializer
