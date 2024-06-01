from django.db import models

class Role(models.Model):
    ROLE_CHOICES = [
        ('Director', 'Director'),
        ('Alumno', 'Alumno'),
        ('Docente', 'Docente'),
        ('Apoderado', 'Apoderado'),
        ('Administrador', 'Administrador'),
    ]
    name = models.CharField(max_length=50, choices=ROLE_CHOICES, unique=True)

    def __str__(self):
        return self.name

class User(models.Model):
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]

    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    dni = models.CharField(max_length=20, unique=True)
    direccion = models.TextField()
    correo = models.EmailField(unique=True)
    genero = models.CharField(max_length=1, choices=GENDER_CHOICES)
    fecha_nacimiento = models.DateField()
    rol = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"