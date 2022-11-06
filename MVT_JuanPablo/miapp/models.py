from django.db import models

class familiares(models.Model):

    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    nacimiento = models.DateField(null=True, blank=True)

