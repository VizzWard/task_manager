# API de Gestión de Tareas Avanzada

(Tecnologías: Django + Django REST Framework (DRF) + MySQL/PostgreSQL)

## 1: Configuración del Proyecto y CRUD Básico

- [x] Configurar el entorno de desarrollo (crear repositorio en GitHub, configurar entorno virtual con venv).
- [x] Definir modelo de datos (Tarea, Usuario, Categoría).
- [x] Implementar autenticación JWT con Django REST Framework SimpleJWT.
- [x] Crear endpoints para CRUD de tareas (crear, leer, actualizar, eliminar).
- [x] Testear con Postman o cURL.

## 2: Roles de Usuario y Notificaciones

- [x] Implementar roles de usuario (admin y usuario normal).
- [x] Proteger los endpoints con permisos adecuados (solo admins pueden eliminar tareas, por ejemplo).
- [x] Configurar Celery (en Django) para enviar notificaciones cuando una tarea esté cerca de su fecha límite.
- [x] Integrar envío de correos usando SMTP o algún servicio como SendGrid.

## 3: Búsqueda y Filtros Avanzados

- [x] Implementar búsqueda de tareas por nombre o descripción.
- [x] Filtrar tareas por categoría, fecha de creación, fecha de vencimiento, etc.
- [x] Paginar resultados y permitir ordenar por diferentes campos.
- [x] Agregar tests automatizados para los filtros y búsquedas.
- [x] Documentar la API con Swagger.

## 4: Exportación y Mejora de la API

- [x] Implementar exportación de tareas a CSV o PDF.
- [x] Optimizar la API (mejorar queries con select_related en Django).
- [x] Escribir tests unitarios y de integración.
- [x] Documentar la API con Swagger.
- [x] Desplegar en un servidor (Render, Railway o VPS con Docker).

# Despliegue

## Consideraciones

### ¿Mantener backend y frontend en el mismo repositorio o separarlos?

La estructura actual `/backend` y `/frontend` es válida para desarrollo, pero hay ventajas y desventajas de separarlos en repos distintos:

✅ Ventajas de separarlos en repos diferentes:

- Permite a los equipos trabajar de manera independiente sin afectar ramas o commits innecesarios.
- Puedes configurar pipelines de CI/CD separados para cada servicio.
- Evita conflictos de dependencias o archivos no relacionados.
- Facilita el despliegue, ya que cada repo puede tener su propia estrategia (por ejemplo, backend en AWS, frontend en Vercel o CloudFront).

❌ Desventajas de separarlos en repos diferentes:

- Puede ser más complicado manejar cambios relacionados entre frontend y backend.
- Requiere más configuración de despliegue y coordinación entre los repos.

### Opción 1: Backend y Frontend separados (Recomendada)

- Backend (Django + MySQL): Se despliega en un servidor (por ejemplo, AWS EC2, Azure App Service, o un contenedor en AWS Fargate/Azure Container Apps).
- Frontend (React): Se despliega en un servicio separado (por ejemplo, AWS S3 + CloudFront, Azure Static Web Apps, o Vercel/Netlify).
- Comunicación: El frontend solo interactúa con el backend a través de los endpoints de la API.

### Opción 2: Backend y Frontend juntos (Monolito)

- Se empaquetan dentro del mismo proyecto.
- Django serviría tanto la API como el frontend (usando Django como servidor de archivos estáticos o con un proxy inverso como Nginx o Caddy).
- Se desplegaría todo en un mismo servidor.

### Sobre la base de datos

#### Opción 1: Base de datos en la misma instancia EC2 (No recomendada)

- Puedes instalar MySQL en la misma EC2 donde corre Django.
- Desventaja: No es escalable ni seguro, si la instancia falla, pierdes la base de datos.

#### Opción 2: Usar AWS RDS (Recomendada)

- AWS RDS (Relational Database Service) te permite crear una base de datos MySQL gestionada.
- Es más seguro, escalable y optimizado.
- Puedes conectar Django con RDS mediante credenciales de entorno.

## Despliegue - Idea Final

1. Backend (Django) → AWS EC2 (o AWS App Runner si quieres serverless).
2. Frontend (React) → Vercel, Netlify o AWS S3 + CloudFront.
3. Base de datos → AWS RDS (MySQL).

Configurar CORS en Django para permitir peticiones desde el frontend.