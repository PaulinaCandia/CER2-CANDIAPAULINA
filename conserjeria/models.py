from django.db import models


class Residencia(models.Model):
    numeroResidencia = models.CharField(max_length=200)
    edificio = models.CharField(max_length=200)

    def __str__(self):
        return "Residencia " + self.numeroResidencia + ", edificio " + self.edificio

class Correspondencia(models.Model):
    residencia = models.ForeignKey(Residencia, on_delete=models.CASCADE)
    destinatario = models.CharField(max_length=200)
    fecha = models.DateTimeField()
    entregado = models.BooleanField(default=False)

    def __str__(self):
        return str(self.residencia) + " " + self.destinatario + " " + str(self.fecha)
