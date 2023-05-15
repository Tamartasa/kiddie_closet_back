import django_filters
from rest_framework.viewsets import ModelViewSet

from kiddie_closet_app.models import Item
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


class ItemFilter(django_filters.FilterSet):
    size_from = django_filters.NumberFilter(field_name='size', lookup_expr='gte')
    size_to = django_filters.NumberFilter(field_name='size', lookup_expr='lte')
    ad = django_filters.CharFilter(field_name='ad__id')
    class Meta:
        model = Item
        fields = {
            'size': ['exact'],
            'category': ['exact'],
            'condition': ['iexact'],
            'gender': ['iexact']
        }


class ItemsViewSet(ModelViewSet):
    queryset = Item.objects.all()
    permission_classes = [ItemPermissions]
    serializer_class = ItemSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = ItemFilter

    def get_queryset(self):
        qs = super().get_queryset()
        qs = self.filter_queryset(qs)  # apply filters
        return qs
