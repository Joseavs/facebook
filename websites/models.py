from django.db import models

# Create your models here.
class cuentas(models.Model):
	nombre = models.CharField(max_length=30)
	apellidos = models.CharField(max_length=30)
