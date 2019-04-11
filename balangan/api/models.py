from django.db import models

class AllBor(models.Model):
    objectid = models.AutoField(primary_key=True)
    nomor = models.DecimalField(max_digits=15, decimal_places=6, blank=True, null=True)
    id_bor = models.CharField(max_length=254, blank=True, null=True)
    x = models.DecimalField(max_digits=15, decimal_places=6, blank=True, null=True)
    y = models.DecimalField(max_digits=15, decimal_places=6, blank=True, null=True)
    z = models.DecimalField(max_digits=15, decimal_places=6, blank=True, null=True)
    depth_from = models.DecimalField(max_digits=15, decimal_places=6, blank=True, null=True)
    depth_bott = models.DecimalField(max_digits=15, decimal_places=6, blank=True, null=True)
    lithologi = models.CharField(max_length=254, blank=True, null=True)
    azimuth = models.CharField(max_length=254, blank=True, null=True)
    inklinasi = models.CharField(max_length=254, blank=True, null=True)
    seam = models.CharField(max_length=254, blank=True, null=True)
    depth = models.DecimalField(max_digits=15, decimal_places=6, blank=True, null=True)
    shape = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'all_bor'


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'


class WwmReklamasi(models.Model):
    objectid = models.AutoField(primary_key=True)
    id = models.IntegerField(blank=True, null=True)
    luasan = models.DecimalField(max_digits=38, decimal_places=8, blank=True, null=True)
    kemiringan = models.IntegerField(blank=True, null=True)
    tinggi = models.IntegerField(blank=True, null=True)
    lebar = models.DecimalField(max_digits=38, decimal_places=8, blank=True, null=True)
    panjang = models.IntegerField(blank=True, null=True)
    shape = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'wwm_reklamasi'