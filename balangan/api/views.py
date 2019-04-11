from django.shortcuts import render
from rest_framework import viewsets
from .models import AllBor, SpatialRefSys, WwmReklamasi
from .serializers import AllBorSer, WwmReklamasiSer

class AllBorView(viewsets.ModelViewSet):
    queryset = AllBor.objects.all()
    serializer_class = AllBorSer

class WwmReklamasiView(viewsets.ModelViewSet):
    queryset = WwmReklamasi.objects.all()
    serializer_class = WwmReklamasiSer
