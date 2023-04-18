from django.urls import path
from rest_framework.routers import DefaultRouter

from kiddie_closet_app.views.neigborhoods import NeighborhoodsViewSet

# automatically defining urls for MoviesViewSet
router = DefaultRouter()
router.register('', NeighborhoodsViewSet)


urlpatterns = [
]

urlpatterns.extend(router.urls)