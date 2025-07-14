# Survey API

API RESTful para la gestión de encuestas, desarrollada con FastAPI y PostgreSQL.

---

## Requisitos

- Docker y Docker Compose

## Configuración

1. Copia el archivo `.env` si no existe. Ya está configurado para usar la base de datos PostgreSQL del contenedor.
2. Instala las dependencias si vas a correr localmente:
   ```sh
   pip install -r requirements.txt
   ```

## Levantar el proyecto con Docker

```sh
docker-compose up --build
```

Esto levantará dos servicios:

- **db**: PostgreSQL persistente en el volumen `surveydb_data`
- **api**: FastAPI en `http://localhost:8000`

Accede a la documentación interactiva de la API en:

- [http://localhost:8000/docs](http://localhost:8000/docs)

## Migraciones con Alembic

Para ejecutar migraciones dentro del contenedor:

```sh
docker-compose exec api alembic upgrade head
```

Para crear una nueva migración:

```sh
docker-compose exec api alembic revision --autogenerate -m "mensaje"
```

### Comandos útiles de Alembic

- **Ver el estado actual de las migraciones:**
  ```sh
  docker-compose exec api alembic current
  ```
- **Ver el historial de migraciones:**
  ```sh
  docker-compose exec api alembic history
  ```
- **Revertir la última migración (rollback):**
  ```sh
  docker-compose exec api alembic downgrade -1
  ```

## Endpoints principales y ejemplos de uso

### 1. Crear encuesta

**POST /surveys**

- **Body:**
  ```json
  {
    "title": "Encuesta de satisfacción",
    "description": "Opcional"
  }
  ```
- **Respuesta:**
  ```json
  {
    "id": 1,
    "title": "Encuesta de satisfacción",
    "description": "Opcional",
    "created_at": "2025-07-14T12:00:00"
  }
  ```

### 2. Agregar pregunta a una encuesta

**POST /surveys/{survey_id}/questions**

- **Body:**
  ```json
  {
    "text": "¿Cómo calificarías el servicio?",
    "question_type": "single_choice" // Puede ser "text", "single_choice" o "multiple_choice"
  }
  ```
- **Respuesta:**
  ```json
  {
    "id": 1,
    "survey_id": 1,
    "text": "¿Cómo calificarías el servicio?",
    "question_type": "single_choice"
  }
  ```

### 3. Agregar opción a una pregunta

**POST /questions/{question_id}/options**

- **Body:**
  ```json
  {
    "text": "Excelente"
  }
  ```
- **Respuesta:**
  ```json
  {
    "id": 1,
    "question_id": 1,
    "text": "Excelente"
  }
  ```
- **Errores posibles:**
  - Si la pregunta no es de tipo elección:
    ```json
    {
      "detail": "Solo se pueden agregar opciones a preguntas de tipo single_choice o multiple_choice"
    }
    ```

---

## Decisiones de Diseño

### 1. Encuestas sin preguntas inicialmente

Se permite la creación de encuestas sin preguntas para facilitar la flexibilidad en el flujo de trabajo. Esto permite crear borradores o plantillas y agregar preguntas posteriormente.

### 2. Definición del tipo de pregunta: Enum

El tipo de pregunta (`text`, `single_choice`, `multiple_choice`) se define como Enum en los modelos y esquemas. Esto garantiza integridad y validación estricta, evitando valores inválidos.

### 3. Validación de opciones según tipo de pregunta

La restricción de que solo preguntas de tipo elección pueden tener opciones se implementa en la lógica de negocio (servicio o endpoint). Antes de agregar una opción, se valida el tipo de la pregunta asociada.

### 4. Ventajas de validar en la lógica de negocio

- Retroalimentación inmediata y clara al usuario de la API.
- Centralización de reglas de negocio, facilitando mantenimiento y evolución.
- Evita inconsistencias que podrían pasar desapercibidas si solo se validara en la base de datos.

### 5. Buenas prácticas aplicadas

- **Estructura modular:** Separación clara entre rutas, modelos, esquemas y servicios.
- **Migraciones con Alembic:** Control de versiones del esquema de base de datos.
- **Variables de entorno (.env):** Configuración desacoplada del código fuente.
- **Entorno Dockerizado:** Aislamiento de dependencias y facilidad de despliegue, con recarga automática del servidor.
- **Documentación:** Instrucciones claras para levantar el entorno y aplicar migraciones.

---

## 🧪 Testing

Para ejecutar los tests automatizados del backend, asegúrate de tener los servicios de Docker levantados y luego ejecuta:

```bash
docker-compose exec api pytest --maxfail=1 --disable-warnings -v
```

Esto ejecutará todos los tests con pytest dentro del contenedor, usando la base de datos de Docker. Los tests validan los endpoints principales, las restricciones de negocio y las validaciones de entrada.

---

## Notas

- La base de datos se llama `surveydb` y los datos persisten en el volumen `surveydb_data`.
- La URL de la base de datos se lee desde `.env`.
