from django.db import models
from django.contrib.auth.models import User
BRANDS = (
    (1, 'Citadel'),
    (2, 'Vallejo'),
    (3, 'Tamiya'),

)

TYPES = (
    (1, 'Regular'),
    (2, 'Wash'),
    (3, 'Ink'),
    (4, 'Contrast'),
    (5, 'Spray'),
    (6, 'Other'),

)


class Paint(models.Model):
    """This model creates paints"""
    name = models.CharField(max_length=64)
    code = models.CharField(null=True, max_length=64)
    brand = models.IntegerField(choices=BRANDS)
    type = models.IntegerField(choices=TYPES)
    analog = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "{} ".format(self.name)
class Collection(models.Model):
    """This model represents collection of paints owned by the user"""
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    contains = models.ManyToManyField(Paint)

class Paint_Sets(models.Model):
    """This model represents paintsets created by the user"""
    name = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paints = models.ManyToManyField(Paint)

    def __str__(self):
        return "{} ".format(self.name)


