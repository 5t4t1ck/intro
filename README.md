# Crear el espacio de trabajo

    Crear un entorno virtual .env
    Crear el archivo requirements.txt
    Agregar el archivo .gitignore

# Activar el entorno virtual

    cd .env/Scripts
    activate

# Agregar en el archivo requirements.txt

    Django==3.1.3

# Instalar Django desde el archivo requirements.txt

    pip install -r requirements.txt

# Comprobar que se encuentra instalado Django

    pip freeze

# Crear un proyecto de Django 

    django-admin startproject Universidad .

# Configurar el archivo settings.py

    cambiar idioma a español y zona horaria
    verificar la zona horaria en wikipedia o en django

# Crear la aplicación académico

    django-admin startapp academico

# Agregar las primeras aplicaciones

    'academico',

# Creamos los primeros modelos

    models.py de academico

    from django.db import models

    class Curso(models.Model):
        codigo=models.CharField(primary_key=True, max_length=6)
	nombre = models.CharField(max_length=50)
	creditos = models.PositiveSmallIntegerField()

# En el archivo admin.py de academico agregar la aplicación creada


    from .models import Curso

    admin.site.register(Curso)

    
# Crear las primeras migraciones

    python manage.py migrate

# Migrar el archivo a la base de datos

    python manage.py makemigrations

# Crear el superusuario de Django

    python manage.py createsuperuser

# Volver a crear las migraciones

    python manage.py migrate

# Obsever el directorio migraciones dentro de académico

# Correr el servidor

    python manage.py runserver

# Verificar que el servidor este corriendo en el navegador

    127.0.0.1:8000

# Verificar en cursos y agregar un curso nuevo desde la administración de Django

# Modificar el método __str__

    def __str__(self):
        texto = "{0} {1}"
        return texto.format(self.nombre, self.creditos)

# Actualizar el navegador y Detener el servidor

    Ctrl + C

# Crear la carpeta llamada templates en la app academico y crear un documento llamado gestionCursos.html y Agregar la siguiente estructura

    <!DOCTYPE html>
    <html lang="en">

    <head>
    	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0"
	<title>Document</title>
    </head>

    <body>
    </body>

    </html>

# Configurar el archivo urls.py en academico

    from django.urls import path
    from . import views

    urlpatterns = [
    path('', views.home)
    ]

# Definir una primera vista en views.py de academico

    from django.shortcuts import render
    from .models import Curso

    def home(request):
        cursosListados = Curso.objects.all()
        return render(request, "gestionCursos.html", {"cursos":cursosListados})
    
# Para verificar que estamos dentro de la vista creada con el template, modificar el archivo gestionCursos.html agregando en el body

    <body>
    <h1>Ya estamos en la gestión de Cursos</h1>
    </body>

# Agregar las rutas en el archivo urls.py de Universidad agregar urlpatterns el path e importar include de django.urls

    from django.urls import path, include

    path('', include("academico.urls")),

# Iniciar el servidor de Django

    python manage.py runserver

