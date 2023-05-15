from kiddie_closet_app.models import Category

# category = Category(category_name='clothes')
# category.save()
from rest_framework.viewsets import ModelViewSet

from kiddie_closet_app.models import Category
from kiddie_closet_app.serializers.categories import CategorySerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()

    serializer_class = CategorySerializer