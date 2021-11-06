from django.db import models

# Create your models here.

class Alumno(models.Model):
    pk_alumno = models.AutoField(primary_key=True, null=False, blank=False)
    carnet = models.CharField(max_length=9, null=False, blank=False)
    nombre = models.CharField(max_length=40, null=False, blank=False)
    carrera = models.TextField(null=False, blank=False)
    imagen1 = models.URLField(max_length=800, default='https://i.postimg.cc/Y0gkNhTM/3aabe0e9a520b9ad90407a82f85adb42.jpg', null=False, blank=False)
    edad = models.DecimalField(null=False, blank=False, max_digits=7, decimal_places=2)

    class Meta:
        verbose_name='alumno'
        verbose_name_plural='alumnos'
        ordering=['nombre']

    def __str__(self):
        return "{0}".format(self.nombre)


class Cursos(models.Model):
    pk_cursos = models.AutoField(primary_key=True, null=False, blank=False)
    horas_curso = models.CharField(max_length=9, null=False, blank=False)
    nombre_cur = models.CharField(max_length=40, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    imagen1_cur = models.URLField(max_length=800, default='https://i.postimg.cc/Y0gkNhTM/3aabe0e9a520b9ad90407a82f85adb42.jpg', null=False, blank=False)
    costo = models.DecimalField(null=False, blank=False, max_digits=7, decimal_places=2)

    class Meta:
        verbose_name='curso'
        verbose_name_plural='cursos'
        ordering=['nombre_cur']

    def __str__(self):
        return "{0}".format(self.nombre_cur)


