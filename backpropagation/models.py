from django.db import models

class data1(models.Model):
    date = models.CharField(max_length=200)
    lowa = models.FloatField(default=0)
    opena = models.FloatField(default=0)
    higha = models.FloatField(default=0)
    closea = models.FloatField(default=0)
    predicatea = models.FloatField(default=0)
