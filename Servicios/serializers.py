from rest_framework import routers, serializers, viewsets
from Servicios.models import Servicios
#from Servicios.models import Servicios2


class ServiciosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Servicios
        fields = ( 'id_user', 'name','date_now', 'status')
"""
class Servicios2Serializers(serializers.ModelSerializer):
    class Meta:
        model = Servicios2
        fields = ( '__all__')"""