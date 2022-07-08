from rest_framework import serializers
from core.models import Promocion

class PromocionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promocion
        fields =['Nombre','Descuento','Porcentaje']