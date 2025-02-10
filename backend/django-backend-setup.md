# Configuración y desarrollo del backend Django

## 1. Configuración inicial

1. Asegúrate de estar en la carpeta `backend` de tu proyecto.
2. Activa tu entorno virtual:
   ```
   source ../.venv/bin/activate  # En Unix
   ..\.venv\Scripts\activate  # En Windows
   ```
3. Instala las dependencias si aún no lo has hecho:
   ```
   pip install -r ../requirements.txt
   ```

## 2. Crear el proyecto Django

Si aún no has creado el proyecto Django:

```
django-admin startproject task_manager .
```

## 3. Configurar la base de datos

1. En `task_manager/settings.py`, configura la base de datos PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_de_tu_db',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

2. Realiza las migraciones iniciales:
   ```
   python manage.py migrate
   ```

## 4. Crear la aplicación API

1. Crea una nueva aplicación Django para tu API:
   ```
   python manage.py startapp api
   ```

2. Añade 'api' y 'rest_framework' a INSTALLED_APPS en `task_manager/settings.py`:

```python
INSTALLED_APPS = [
    # ...
    'rest_framework',
    'api',
]
```

## 5. Definir modelos

En `api/models.py`, define tus modelos. Por ejemplo:

```python
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
```

Después de definir tus modelos, crea y aplica las migraciones:
```
python manage.py makemigrations
python manage.py migrate
```

## 6. Crear serializadores

En `api/serializers.py`:

```python
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'created_at', 'user']
```

## 7. Crear vistas

En `api/views.py`:

```python
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
```

## 8. Configurar URLs

1. En `task_manager/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
```

2. Crea `api/urls.py`:

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

## 9. Configurar autenticación (opcional)

Si quieres añadir autenticación, puedes usar JWT. Añade esto a `task_manager/settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}
```

## 10. Probar la API

1. Crea un superusuario:
   ```
   python manage.py createsuperuser
   ```

2. Inicia el servidor de desarrollo:
   ```
   python manage.py runserver
   ```

3. Visita `http://localhost:8000/api/` para ver y probar tu API.
