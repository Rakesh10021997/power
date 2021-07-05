from django.shortcuts import render
from fusion.models import Dress
from fusion.serializers import DressSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.
class DressCRUDCBV(ModelViewSet):
    queryset=Dress.objects.all()
    serializer_class=DressSerializer