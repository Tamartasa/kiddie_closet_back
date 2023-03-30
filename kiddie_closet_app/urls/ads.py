from rest_framework.routers import DefaultRouter

from kiddie_closet_app.views.ads import AdsViewSet

# automatically defining urls for MoviesViewSet
router = DefaultRouter()
router.register('', AdsViewSet)


urlpatterns = [
]

# adding movies urls to urlpatterns
urlpatterns.extend(router.urls)