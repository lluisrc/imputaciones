from django.db import models
from django.urls import reverse
from datetime import date

class Registro(models.Model):
    dia = models.DateField(null=True, blank=True)
    entrada = models.TimeField(null=True, blank=True)
    comida = models.TimeField(null=True, blank=True)
    llegada = models.TimeField(null=True, blank=True)
    salida = models.TimeField(null=True, blank=True)

    # Cuando un vista generica update guarda los cambios del form busca la funcion get_absolute_url() para hacer el redirect
    def get_absolute_url(self):
        return reverse('registro-update', args=[str(self.id)])

    def get_absolute_url_update(self):
        return reverse('registro-update', args=[str(self.id)])
