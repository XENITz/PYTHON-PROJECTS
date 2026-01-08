# 🏭 Proyecto: Industrial IoT Gateway API
**Estado:** Fase 1 (Ingesta y Validación)
**Rol:** Backend Engineer

---

### 📋 Contexto del Negocio
Somos una fábrica manufacturera moderna. Tenemos cientos de sensores y PLCs (Controladores Lógicos Programables) en la planta. Actualmente, los datos están aislados en cada máquina.

Necesitamos un sistema centralizado (**Gateway**) que reciba lecturas de temperatura, presión y estado en tiempo real a través de HTTP para su posterior análisis.

**Tu misión:** Crear la API que actuará como el punto de entrada seguro, validado y robusto para estos datos.

---

### 🛠️ Requisitos Técnicos (The Stack)
* **Lenguaje:** Python 3.10+
* **Framework:** FastAPI
* **Servidor:** Uvicorn (ASGI)
* **Gestión de Entorno:** Virtual Environment (`venv`)
* **Control de Versiones:** Git (Repo local)
* **Testing:** cURL / Postman (Prohibido usar navegador para testing)

---

### 🎯 Objetivos de la Fase 1

#### 1. Arquitectura Base
* Inicializar un repositorio de Git (`git init`).
* Crear un entorno virtual aislado (`python -m venv venv`).
* Estructura de carpetas profesional:
  ```text
  /iot-gateway
  ├── venv/
  ├── main.py          # Punto de entrada de la app
  ├── requirements.txt # Lista de dependencias
  └── README.md        # Documentación

# 🏭 Proyecto: Industrial IoT Gateway API
**Estado:** Fase 2 (Seguridad y Persistencia)
**Rol:** Backend & Security Engineer

---

### 📋 Contexto del Negocio (Update)
La Fase 1 fue un éxito, pero Seguridad Corporativa ha detectado una vulnerabilidad crítica: **el endpoint es público**. Cualquier persona en la red WiFi podría enviar datos falsos de temperatura y provocar una parada de emergencia en la fábrica.

Además, el equipo de Análisis de Datos se queja de que los datos solo aparecen en la consola y desaparecen. Necesitamos guardarlos permanentemente.

**Tu misión:**
1.  Implementar un sistema de **Autenticación (API Key)** para asegurar que solo las máquinas autorizadas envíen datos.
2.  Implementar una **Base de Datos SQL** para persistir el histórico de lecturas.

---

### 🛠️ Nuevas Herramientas (Tech Stack)
* **Base de Datos:** SQLite (Local) usando **SQLAlchemy** (ORM).
* **Seguridad:** FastAPI `Security` y `HTTPBearer`.
* **Criptografía:** `Passlib` (Opcional, para hashing futuro).

---

### 🎯 Objetivos de la Fase 2

#### 1. La Capa de Persistencia (Base de Datos)
* No vamos a escribir SQL crudo (`INSERT INTO...`). Usaremos un **ORM (Object Relational Mapper)**.
* **Instalar:** `pip install sqlalchemy`
* **Tarea:** Configurar `database.py`.
* **Modelo DB:** Crear una tabla llamada `readings` con las columnas:
    * `id` (Integer, Primary Key, Autoincrement)
    * `machine_id` (String)
    * `temperature` (Float)
    * `pressure` (Float)
    * `timestamp` (DateTime, Default=Now)

#### 2. La Capa de Seguridad (The Bouncer)
* Las máquinas no tienen usuario y contraseña, usan **API Keys**.
* **Tarea:** Crear una dependencia de seguridad.
* La API debe buscar un **Header** específico en cada petición:
    * `x-api-key: SECTRET-SUPER-SECURE-KEY-123`
* Si el Header no existe o la clave es incorrecta, rechazar inmediatamente.

#### 3. Conexión End-to-End
* Modificar el endpoint `POST /sensor-data`:
    1.  **Validar:** (Ya hecho en Fase 1).
    2.  **Autenticar:** Verificar la API Key (Nuevo).
    3.  **Persistir:** Guardar el objeto en el archivo `industrial.db` (Nuevo).
    4.  **Responder:** Confirmar el guardado.

---

### 🛡️ Reglas de Seguridad (Hard Rules)
1.  **Cero Confianza:** Si una petición llega sin el Header de seguridad, la respuesta debe ser **HTTP 401 Unauthorized** o **HTTP 403 Forbidden**. No debe procesarse nada más.
2.  **Inyección SQL:** Al usar SQLAlchemy, estamos protegidos, pero asegúrate de nunca concatenar strings en las consultas.

---

### ✅ Criterios de Aceptación (Definition of Done)

Para aprobar esta fase, debes realizar las siguientes pruebas en tu terminal (`curl`):

1.  [ ] **Prueba de Intruso (Sin Llave):**
    * Intentar enviar datos sin el Header `x-api-key`.
    * **Resultado:** Error 401/403.
2.  [ ] **Prueba de Intruso (Llave Falsa):**
    * Enviar `x-api-key: hacker-123`.
    * **Resultado:** Error 401/403.
3.  [ ] **Prueba de Acceso Autorizado:**
    * Enviar `x-api-key: SECTRET-SUPER-SECURE-KEY-123` (o la que definas).
    * **Resultado:** HTTP 200 OK.
4.  [ ] **Prueba de Persistencia:**
    * Enviar 3 datos válidos seguidos.
    * Reiniciar el servidor (apagar y prender `uvicorn`).
    * Instalar un visor de SQLite (o usar una extensión de VS Code como "SQLite Viewer").
    * Abrir el archivo `.db` y verificar que las 3 filas sigan ahí.

---

### 🔥 Hardcore Mode (Reto Extra)
*Solo para ingenieros avanzados.*

* **Dependency Injection:** No escribas la lógica de la base de datos dentro de la función del endpoint (`def receive_data`).
* Crea una función `get_db()` que use `yield` para abrir y cerrar la conexión a la base de datos automáticamente en cada petición.
* Inyéctala en tu ruta: `def receive_data(data: SensorData, db: Session = Depends(get_db))`.