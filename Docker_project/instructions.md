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