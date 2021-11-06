from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    allAlumno = Alumno.objects.all()
    allCursos = Cursos.objects.all()
    return render(request, 'index.html', {'allBebidas':allAlumno,
                                          'allExtras':allCursos})

def Contact(request):
    return render(request, 'contact.html')


def About(request):
    return render(request, 'about.html')

def Blog(request):
    return render(request, 'blog.html')

def Curso(request):
    return render(request, 'course-grid-2.html')