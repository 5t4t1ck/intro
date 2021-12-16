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
    from . import views

    path('', include("academico.urls")),

# Iniciar el servidor de Django

    python manage.py runserver

# Modificar el archivo views.py de academico.

views.py

    from .models import Curso

    def home(request):
        cursosListados = Curso.objects.all()
        messages.success(request, '¡Cursos listados!')
        return render(request, "gestionCursos.html", {"cursos": cursosListados})

# En el archivo gestionCursos.html incluir

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <h1>
            Ya estamos en la página de Gestión de Cursos
        </h1>
        <ul>
            {% for c in cursos %}
            <li>
                {{c.nombre}}
            </li>
            {% endfor %}

        </ul>
    </body>
    </html>

Refrescamos el navegador con F5

# Nuestro primer encuentro con el Framework Bootstrap 

    https://getbootstrap.com

# Copiar el archivo CSS y JavaScript de Bootstrap en el archivo gestionCursos.html

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>

    <!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

    </head>
    <body>
        <h1>
            Ya estamos en la página de Gestión de Cursos
        </h1>
        <ul>
            {% for c in cursos %}
            <li>
                {{c.nombre}}
            </li>
            {% endfor %}

        </ul>

    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>



    </body>
    </html>

Refrescamos el navegador con F5

# Crear base.html en templates para comprender el tema herencia de plantillas

Seleccionar todo lo que está en el archivo gestionCursos.html y copiar en el archivo base.html

# Copiar todo lo que se encuentra en la sección <body> </body>, excepto lo de JavaScript

    <h1>
        Ya estamos en la página de Gestión de Cursos
    </h1>
    <ul>
        {% for c in cursos %}
        <li>
            {{c.nombre}}
        </li>
        {% endfor %}

    </ul>

# Pegar en el archivo base.html lo copiado anteriormente y agregar entre <body> y las etiquetas de javascript lo siguiente

    {% block body %}

    {% endblock %}

Dejar el <tittle></title> bacio

# En el archivo gestionCursos.html agregar

    {% extends "./base.html" %}

    {% block title %} Gestión de Cursos {% endblock %}

    {% block body %}

# Agregar la Barra de Navegación en Bootstrap

En la componentes elegir Navar una barra de navegación sencilla que se la debe pegar antes de {% block body %} en el archibo base.html

    <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
        <a class="navbar-brand" href="#">Navbar</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
            <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
            </li>
            <li class="nav-item">
            <a class="nav-link" href="#">Features</a>
            </li>
            <li class="nav-item">
            <a class="nav-link" href="#">Pricing</a>
            </li>
            <li class="nav-item">
            <a class="nav-link disabled">Disabled</a>
            </li>
        </ul>
        </div>
    </div>
    </nav>

Eliminar algunas etiquetas, solo dejar Universidad, Home y podría ser contactos o la que ud elija

# Actualizamos el navegador F5

# SEGUIMOS...

# Dentro de {% block body %} y {% endblock %} en el archibo gestionCursos.html poner:

    <h1> Esto es parte de Gestion de Cursos </h1>

De esta forma podemos ver como funcionan las plantillas

# En el archivo base cambiar en <title></title> el siguiente código

    {% block title}
    {% endblock %}

# Y en gestionCursos.html tambien cambiar en <title></title>

    {% block title}
    Gestion de Cursos
    {% endblock %}
