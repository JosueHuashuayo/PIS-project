from django.db import models

# Create your models here.

from django.db import models

class Institucion(models.Model):
    # id_director_general = models.ForeignKey('Director', on_delete=models.CASCADE)
    codigo_ie = models.CharField(max_length=20, unique=True)
    vision = models.TextField()
    mision = models.TextField()
    direccion = models.TextField()
    nombre = models.TextField()
    programa_educativo = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='instituciones_educativas')
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    

class RedSocial(models.Model):
    institucion_educativa = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    nombre_red_social = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logo_redes_sociales')
    url = models.URLField()

class Sede(models.Model):
    institucion_educativa = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    nombre_sede = models.CharField(max_length=255)
    direccion = models.TextField()
    latitud = models.DecimalField(max_digits=9, decimal_places=6)
    longitud = models.DecimalField(max_digits=9, decimal_places=6)
    imagen_sede = models.ImageField(upload_to='sedes')
    horario_atencion = models.TextField()
    publicado = models.BooleanField(default=False)
