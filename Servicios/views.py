from django.shortcuts import render
# ----------------MODELOS-----------------
from Servicios.models import Servicios
# ----------------SERIALIZER--------------
from Servicios.serializers import ServiciosSerializers

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.shortcuts import get_object_or_404

from Servicios.models import Servicios as ServiciosModel
from Servicios.serializers import ServiciosSerializers

# from django.


class Servicios(APIView):
    def get(self, request, format=None):
        queryset = ServiciosModel.objects.filter(status=False)
        serializer = ServiciosSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ServiciosSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            response = datas
            return Response(response, status=status.HTTP_201_CREATED)
        response = serializer.errors
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class Servicios2(APIView):
    """def delete(self, request, pk):
        producto = get_object_or_404(Servicios.objects.all(), pk=pk)
        producto.delete()
        return Response({"message": "Product with id '{}' has been deleted".format(pk)}, status=204)"""

    def get_object(self, pk):
        try:
            return ServiciosModel.objects.get(pk=pk, status=False)
        except ServiciosModel.DoesNotExist:
            return False

    def get(self, request, pk, format=None):
        Servicios = self.get_object(pk)
        if Servicios != False:
            serializer = ServiciosSerializers(Servicios)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        ServiciosModel.objects.filter(pk=pk).update(status=True)
        return Response("ok")

    def put(self, request, pk, format=None):
        Servicios = self.get_object(pk)
        if Servicios != False:
            serializer = ServiciosSerializers(Servicios, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
