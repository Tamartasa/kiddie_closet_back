from django.urls import path, include
from rest_framework.routers import DefaultRouter

from kiddie_closet_app.views.categories import CategoryViewSet


router = DefaultRouter()
router.register('', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

