from rest_framework.routers import DefaultRouter

from kiddie_closet_app.views.items import ItemsViewSet

# automatically defining urls for MoviesViewSet
router = DefaultRouter()
router.register('', ItemsViewSet)


urlpatterns = [
]

# adding movies urls to urlpatterns
urlpatterns.extend(router.urls)