from rest_framework.viewsets import ModelViewSet

from kiddie_closet_app.models import Ad, Item
from kiddie_closet_app.serializers.ads import AdSerializer
from kiddie_closet_app.serializers.items import ItemSerializer


class ItemPermissions(BaseException):
    # Get all items - available for all

    # Add new item - available for logged-in users
    def has_permission(self, request, view):
        if request.method in ['POST']:
            return request.user.is_authenticated
        return True

    # Update item - available only for logged-in staff users or
    # non-staff logged-in user that published the item
    def has_object_permission(self, request, view, obj):
        if request.method in ['PATCH', 'PUT', 'DELETE']:
            return request.user.is_authenticated and request.user.is_staff or\
                    request.user.is_authenticated and request.user.id == obj.user_id
        return True

class ItemsViewSet(ModelViewSet):
    queryset = Item.objects.all()

    permission_classes = [ItemPermissions]

    serializer_class = ItemSerializer

    # Get all items or search item by field
    def get_queryset(self):
        qs = Item.objects.all()
        if self.action == 'list':
            # by category
            category = self.request.query_params.get('category')
            if category:
                qs = qs.filter(category_id__exact=category)

            size = self.request.query_params.get('size')
            if size:
                qs = qs.filter(size__exact=size)

            condition = self.request.query_params.get('condition')
            if condition:
                qs = qs.filter(condition__iexact=condition)

            gender = self.request.query_params.get('gender')
            if gender:
                qs = qs.filter(gender__iexact=gender)


        return qs

