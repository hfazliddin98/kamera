from django.db import models

class Fakultet(models.Model):
    fakultet = models.CharField(max_length=100)
    link = models.CharField(max_length=700)
    nomer = models.CharField(max_length=300)
    yoqish = models.CharField(max_length=100, blank=True)
