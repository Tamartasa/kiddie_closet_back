from requests import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from kiddie_closet_app.models import Neighborhood
from kiddie_closet_app.serializers.neighborhoods import NeighborhoodSerializer

class NeighborhoodsViewSet(ModelViewSet):
    queryset = Neighborhood.objects.all()

    # permission_classes = [NeighborhoodPermissions]

    serializer_class = NeighborhoodSerializer

    def create(self, request, *args, **kwargs):
        # Check if a neighborhood with the same name already exists in the database
        name = request.data.get('name')
        existing_neighborhoods = Neighborhood.objects.filter(name=name)
        if existing_neighborhoods.exists():
            # Delete all duplicate neighborhoods and keep the first one
            for neighborhood in existing_neighborhoods[1:]:
                neighborhood.delete()
            print(f"{existing_neighborhoods.count() - 1} duplicates of neighborhood {name} deleted from database.")
            return Response({
                                "message": f"{existing_neighborhoods.count() - 1} duplicates of neighborhood {name} deleted from database."})

        # If the neighborhood doesn't exist yet, create it
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        print(f"neighborhood {name} saved to database.")
        return Response
