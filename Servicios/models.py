from django.db import models
from django.utils import timezone

class Servicios(models.Model):
    #example2 = models.ManyToManyField(Servicio2, related_name='Example2')
    #name = models.CharField(max_length=255, null=False)
    #img = models.ImageField(upload_to='media/', null=True)
    id_user = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254)
    date_now = models.DateTimeField( default=timezone.now)
    status = models.BooleanField(default=False)

    class Meta:
        db_table = "Services"
"""
class Servicios2(models.Model):
    example = models.ForeignKey(Servicios2, on_deelete)
    name =  models.CharFieldmax_length=254()
    delete =  models"""

    #Generar un ejemplo de la relación manytomanyField
    #Generar un ejemplo de la relación OneToMany, ForeignKey
