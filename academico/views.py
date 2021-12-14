from django.shortcuts import render
from .models import Curso

def home(request):
    cursosListados = Curso.objects.all()
    return render(request, "gestionCursos.html", {"cursos":cursosListados})