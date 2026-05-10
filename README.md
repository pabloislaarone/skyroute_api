# ✈️ SkyRoute API

API REST desarrollada con Django y Django REST Framework para gestionar vuelos y aerolíneas.

Permite realizar CRUD completo, búsqueda y relación entre entidades.

---

## 🚀 Tecnologías
- Python
- Django
- Django REST Framework
- SQLite

---

## ⚙️ Ejecución

git clone https://github.com/pabloislaarone/skyroute_api.git  
cd skyroute_api  
python -m venv venv  
venv\Scripts\activate  
pip install django djangorestframework  
python manage.py migrate  
python manage.py runserver  

---

## 📌 Endpoints

### Aerolíneas
- GET /api/aerolineas/
- POST /api/aerolineas/

Ejemplo:
{
  "nombre": "LATAM",
  "pais_origen": "Chile"
}

---

### Vuelos
- GET /api/vuelos/
- POST /api/vuelos/

Ejemplo:
{
  "codigo": "LA123",
  "origen": "Lima",
  "destino": "Cusco",
  "aerolinea": 1
}

---

## 🔍 Búsqueda

GET /api/vuelos/?search=Lima

---

## ⭐ Extra

Se incluye el campo `aerolinea_nombre` en la respuesta.

---

## 🧪 Pruebas

### Aerolíneas
![Aerolíneas](docs/aerolineas.png)

### Vuelos
![Vuelos](docs/vuelos.png)

### Crear vuelo
![Crear](docs/crear_vuelo.png)

### Búsqueda
![Búsqueda](docs/busqueda.png)

---

## 🐙 Repo
https://github.com/pabloislaarone/skyroute_api