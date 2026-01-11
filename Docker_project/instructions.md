# 🚌 Proyecto: Monterrey Transit Core (MTC)
**Versión:** 0.1.0 (Alpha)
**Estado:** Fase 1 - Estructura de Rutas Estáticas
**Rol:** Backend Architect

---

### 📋 Visión del Producto
Crear una API Open Source de alto rendimiento que sirva como la "verdad absoluta" del transporte público en Monterrey.
En esta primera etapa, no rastrearemos camiones en vivo. Primero necesitamos construir el **Mapa Digital**: definir qué rutas existen y dónde están sus paradas.

**Objetivo del Fin de Semana:**
Construir una API REST que permita dar de alta Rutas (ej. "Ruta 400") y sus Paradas asociadas, guardando todo en una Base de Datos Relacional y validando que las coordenadas pertenezcan a Nuevo León.

---

### 🛠️ Tech Stack (Herramientas)
* **Lenguaje:** Python 3.10+
* **Core:** FastAPI (Velocidad y Documentación).
* **Base de Datos:** SQLite (Por simplicidad en Fase 1) -> Migraremos a PostgreSQL en Fase 2.
* **ORM:** SQLModel o SQLAlchemy (Para manejar la relación "Una Ruta tiene Muchas Paradas").
* **Validación:** Pydantic (Para asegurar coordenadas reales).

---

### 🏛️ Arquitectura de Datos (Database Schema)

Necesitas diseñar 2 tablas principales con una relación **Uno-a-Muchos (1:N)**.



#### 1. Tabla `routes` (Padre)
Representa la línea de camión.
* `id` (Integer, PK): Autoincremental.
* `internal_code` (String, Unique): Ej: "R400-P".
* `name` (String): Ej: "Ruta 400 - Sector 1 por Pioneros".
* `status` (Enum): "active", "suspended".

#### 2. Tabla `stops` (Hijo)
Representa los puntos geográficos donde sube gente.
* `id` (Integer, PK): Autoincremental.
* `route_id` (Integer, FK): **Foreign Key** que conecta con `routes.id`.
* `name` (String): Ej: "Av. Cuauhtémoc y 5 de Mayo".
* `latitude` (Float): Coordenada Y.
* `longitude` (Float): Coordenada X.
* `sequence` (Integer): Orden de la parada (1, 2, 3...).

---

### 🎯 Objetivos Técnicos (Sábado & Domingo)

#### Misión 1: El Modelo y el Motor (Backend Logic)
* Configurar el proyecto FastAPI.
* Definir los Modelos en SQLAlchemy/SQLModel.
* **Reto de Ingeniería:** Configurar la relación (`relationship`) para que cuando pidas una Ruta, la DB traiga automáticamente sus paradas.

#### Misión 2: Endpoints Administrativos (CRUD)
* `POST /routes`: Crear una nueva ruta.
* `POST /routes/{id}/stops`: Agregar una parada a una ruta existente.
* `GET /routes/{id}`: Obtener la info de la ruta.
* `GET /routes/{id}/full-map`: **Endpoint Clave.** Debe devolver un JSON anidado con la ruta y la lista de todas sus paradas ordenadas por secuencia.

#### Misión 3: Validación Geográfica (Business Logic)
* Monterrey y su área metropolitana están aproximadamente entre:
    * **Latitud:** 25.30 a 26.00
    * **Longitud:** -100.80 a -99.80
* **Regla:** Si intentas crear una parada fuera de este rango, la API debe rechazarla con un `400 Bad Request` y el mensaje: *"Coordinates out of Monterrey Metropolitan Area"*.

---

### 🤖 Frontend (Delegado a IA)
*Al terminar el backend, pedirás a Claude/ChatGPT:*
> "Genera un archivo `index.html` único que use Leaflet.js. Debe consumir mi endpoint local `GET /routes/1/full-map` y pintar las paradas como marcadores azules en un mapa de OpenStreetMap centrado en Monterrey."

---

### ✅ Definition of Done (Criterios de Aceptación)

Para considerar el fin de semana exitoso, debes poder ejecutar este flujo en tu terminal:

1.  **Crear Ruta:**
    `POST` -> Crea la "Ruta 214". Recibe ID `1`.
2.  **Agregar Paradas:**
    `POST` -> Agrega "Parada Tec" (Lat: 25.65, Lon: -100.29) a la Ruta `1`.
    `POST` -> Agrega "Parada Centro" a la Ruta `1`.
3.  **Validación:**
    `POST` -> Intenta agregar una parada en China (Lat: 35.0, Lon: 110.0). -> **Error 400**.
4.  **Visualización:**
    Abres el `index.html` generado por IA y ves los puntos pintados sobre el mapa de Monterrey.

---

### 📅 Agenda Sugerida

* **Sábado (Construction):** Definir modelos DB, crear tablas y endpoints POST.
* **Domingo (Integration):** Validaciones de latitud/longitud, endpoint GET anidado y prueba visual con el HTML generado.