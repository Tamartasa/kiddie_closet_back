from rest_framework.viewsets import ModelViewSet

from kiddie_closet_app.models import Neighborhood
from kiddie_closet_app.serializers.neighborhoods import NeighborhoodSerializer


# class NeighborhoodPermissions(BaseException):
#     # Get all neighborhoods - available for staff only
#
#     def has_permission(self, request, view):
#         return request.user.is_authenticated and request.user.is_staff
#
#     def has_object_permission(self, request, view, obj):
#         return request.user.is_authenticated and request.user.is_staff


class NeighborhoodsViewSet(ModelViewSet):
    queryset = Neighborhood.objects.all()

    # permission_classes = [NeighborhoodPermissions]

    serializer_class = NeighborhoodSerializer