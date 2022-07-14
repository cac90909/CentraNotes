from django.urls import include, path

from rest_framework import routers

from TestApi.views import CountryViewSet, CityViewSet

router = routers.DefaultRouter()
router.register(r'country', CountryViewSet)
router.register(r'city', CityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]