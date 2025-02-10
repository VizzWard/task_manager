import os
import sys
import django
from django.db import connections
from django.db.utils import OperationalError

# Añade la ruta del proyecto al PYTHONPATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Configura los settings de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "task_manager.settings")
django.setup()

try:
    conn = connections['default']
    conn.cursor()
    print("Conexión exitosa a la base de datos.")
except OperationalError:
    print("No se pudo conectar a la base de datos.")