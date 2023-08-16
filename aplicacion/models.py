from django.db import models
from django.contrib.auth.models import User


#__________Modelos Utilizados en página_____________________


class Clases(models.Model):
    nombre = models.CharField(max_length=50)
    dia = models.CharField(max_length=50)
    hora = models.CharField(max_length=50)
    valor = models.IntegerField()

    class Meta:
        verbose_name_plural = "Clases"   

    def __str__(self):
        return f"{self.nombre},{self.dia},{self.hora}, {self.valor}"



class Profesores(models.Model):
    nombre =models.CharField(max_length=50)
    clase = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Profesores"

    def __str__(self):
        return f"{self.nombre},{self.clase}"
    


class Alumnos(models.Model):
    nombre =models.CharField(max_length=50)
    mail = models.EmailField(max_length=254)
    edad = models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Alumnos"

    def __str__(self):
        return f"{self.nombre},{self.edad},{self.mail}"



class Sedes(models.Model):
    direccion =models.CharField(max_length=50)
    numeracion = models.IntegerField()

    class Meta:
        verbose_name_plural = "Sedes"

    def __str__(self):
        return f"{self.direccion}  N°{self.numeracion}"
    

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete= models.CASCADE)

    class Meta:
        verbose_name_plural = "Avatar"
   
    def __str__(self):
        return f"{self.user} [{self.imagen}]"

