from django.db import models

# Create your models here.
class RazzakModel(models.Model):
    razzak_not = models.CharField(max_length=200)

class ParthoModel(models.Model):
    partho_not = models.CharField(max_length=200)

class RiadulModel(models.Model):
    riadul_not = models.CharField(max_length=200)

class TariqulModel(models.Model):
    tariqul_not = models.CharField(max_length=200)

class ShaonModel(models.Model):
    shaon_not = models.CharField(max_length=200)

class MasudModel(models.Model):
    masud_not = models.CharField(max_length=200)

class ShahinModel(models.Model):
    shahin_not = models.CharField(max_length=200)

class MuntasirModel(models.Model):
    muntasir_not = models.CharField(max_length=200)

class RafiModel(models.Model):
    rafi_not = models.CharField(max_length=200)

class ZahidModel(models.Model):
    zahid_not = models.CharField(max_length=200)



class NoticeModel(models.Model):
    notice = models.CharField(max_length=200)

