from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ResourceAlumno(resources.ModelResource):
    class Meta:
        model = Alumno

class AdminAlumno(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['pk_alumno', 'carnet', 'nombre', 'carrera', 'edad']
    resource_class = ResourceAlumno

admin.site.register(Alumno, AdminAlumno)

class ResourceCursos(resources.ModelResource):
    class Meta:
        model = Cursos

class AdminCursos(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre_cur']
    list_display = ['pk_cursos', 'horas_cur', 'nombre_cur', 'descripcion', 'costo']
    resource_class = ResourceCursos

admin.site.register(Cursos, AdminCursos)