from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('regions', RegionViewSet)
router.register('districts', DistrictViewSet)
router.register('communes', CommuneViewSet)
router.register('fokontanys', FokontanyViewSet)
router.register('electeurs', ElecteurViewSet)

urlpatterns = [
    path('', include(router.urls)),
]