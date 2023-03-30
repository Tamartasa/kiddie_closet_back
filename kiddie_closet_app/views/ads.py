from rest_framework.viewsets import ModelViewSet

from kiddie_closet_app.models import Ad
from kiddie_closet_app.serializers.ads import AdSerializer

# class AdPermissions(BaseException):
#
# def has_permission(self, request, view):
#     if request.method in ['POST', 'PUT', 'PATCH']:
#         return request.user.is_staff and request.user.is_authenticated
#     return True
#
#
# def has_object_permission(self, request, view, obj):
#     if request.method in ['PATCH', 'PUT', 'DELETE']:
#         return request.user.is_authenticated and request.user.is_staff
#     return True

class AdsViewSet(ModelViewSet):
    queryset = Ad.objects.all()

    permission_classes = []

    serializer_class = AdSerializer
