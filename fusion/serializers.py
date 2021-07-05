from fusion.models import Dress 
from rest_framework.serializers import ModelSerializer
class DressSerializer(ModelSerializer):
    class Meta:
        model=Dress
        fields='__all__'