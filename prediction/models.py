
from django.db import models

class data(models.Model):
    date = models.CharField(max_length=200)
    gold = models.FloatField(default=0)
    nasdaq = models.FloatField(default=0)
    oil = models.FloatField(default=0)
    usdnpr = models.FloatField(default=0)
    predicate = models.FloatField(default=0)


class login(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

