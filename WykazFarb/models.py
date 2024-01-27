from django.db import models
from django.contrib.auth.models import User

BRANDS = (
    (1, 'Citadel'),
    (2, 'Vallejo Game Color'),
    (3, 'Vallejo Game Air'),
    (4, 'Old Citadel'),
    (4, 'Tamiya'),

)

TYPES = (
    (1, 'Regular'),
    (2, 'Wash'),
    (3, 'Ink'),
    (4, 'Contrast'),
    (5, 'Spray'),
    (6, 'Other'),

)
class New_Paint_Analogs(models.Model):
    """This class creates paints and their analogs"""
    New_Citadel = models.CharField(null=True, max_length=64)
    Old_Citadel = models.CharField(null=True, max_length=64)
    Vallejo_Game_Color = models.CharField(null=True, max_length=64)
    VGC_Code = models.FloatField(null=True, max_length=64)
    Vallejo_Model_Color = models.CharField(null=True, max_length=64)
    VMC_Code = models.FloatField(null=True, max_length=64)
    Vallejo_Model_Air = models.CharField(null=True, max_length=64)
    VMA_Code = models.FloatField(null=True, max_length=64)
    Rackham = models.CharField(null=True, max_length=64)
    Privateer_Press = models.CharField(null=True, max_length=64)
    Hex_Code = models.CharField(null=True, max_length=64)


class Paint(models.Model):
    """This model creates paints"""
    name = models.CharField(max_length=64)
    code = models.CharField(null=True, max_length=64)
    brand = models.IntegerField(choices=BRANDS)
    type = models.IntegerField(choices=TYPES, null=True)
    hex = models.ForeignKey(New_Paint_Analogs, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "{} ".format(self.name)


class Paint_Sets(models.Model):
    """This model represents paintsets created by the user"""
    name = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    paints = models.ManyToManyField(Paint)
class Collection(models.Model):
    """This model represents collection of paints owned by the user"""
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    contains = models.ManyToManyField(Paint)

class Element(models.Model):
    name = models.CharField(max_length=64)
    paints = models.ManyToManyField(Paint)
    paint_sets = models.ForeignKey(Paint_Sets, on_delete=models.CASCADE, null=True)
