from rest_framework import viewsets
from .models import Region, District, Commune, Fokontany, Electeur
from .serializers import *

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
class CommuneViewSet(viewsets.ModelViewSet):
    queryset = Commune.objects.all()
    serializer_class = CommuneSerializer
class FokontanyViewSet(viewsets.ModelViewSet):
    queryset = Fokontany.objects.all()
    serializer_class = FokontanySerializer
class ElecteurViewSet(viewsets.ModelViewSet):
    queryset = Electeur.objects.all()
    serializer_class = ElecteurSerializer

    def get_queryset(self):
        queryset = Electeur.objects.all()
        region_id = self.request.query_params.get('region')
        district_id = self.request.query_params.get('district')  # 🆕
        commune_id = self.request.query_params.get('commune')
        fokontany_id = self.request.query_params.get('fokontany')

        if region_id:
            queryset = queryset.filter(fokontany__commune__district__region__id_region=region_id)
        if district_id:
            queryset = queryset.filter(fokontany__commune__district__id_district=district_id)
        if commune_id:
            queryset = queryset.filter(fokontany__commune__id_commune=commune_id)
        if fokontany_id:
            queryset = queryset.filter(fokontany__id_fokontany=fokontany_id)

        return queryset

