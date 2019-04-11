from rest_framework import serializers
from .models import AllBor, SpatialRefSys, WwmReklamasi


class AllBorSer(serializers.ModelSerializer):
    class Meta:
        model = AllBor
        fields = (
            'objectid',
            'nomor',
            'id_bor',
            'x',
            'y',
            'z',
            'depth_from',
            'depth_bott',
            'lithologi',
            'azimuth',
            'inklinasi',
            'seam',
            'depth',
            'shape',
        )

class WwmReklamasiSer(serializers.ModelSerializer):
    class Meta:
        model = WwmReklamasi
        fields = (
            'objectid',
            'id',
            'luasan',
            'kemiringan',
            'tinggi',
            'lebar',
            'panjang',
            'shape'
        )

