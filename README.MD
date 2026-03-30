# 🚜 Mining Telemetry Data Pipeline (End-to-End)

Este proyecto implementa una arquitectura de datos completa (Pipeline ETL) para el monitoreo de telemetría en tiempo real de maquinaria pesada (Camiones CAT 797F) en operaciones mineras.

## Descripción del Proyecto
El sistema simula la ingesta de datos de sensores IoT, los organiza en un **Data Lake** bajo la arquitectura de Medallón, los procesa mediante un flujo **ETL** y los visualiza en un **Dashboard interactivo** para la toma de decisiones preventivas.

## Arquitectura del Sistema
1. **Ingesta (Capa Bronze):** Generador de datos en Python que simula telemetría (GPS, Temperatura, RPM, Combustible) en formato JSON.
2. **Procesamiento (Capa Silver):** Script ETL que limpia, valida y transforma los datos crudos, aplicando lógica de negocio para detectar alertas críticas (>95°C).
3. **Almacenamiento:** Base de Datos SQL (MySQL) estructurada para consultas analíticas de alto rendimiento.
4. **Visualización (Capa Gold):** Dashboard en tiempo real con Streamlit que muestra KPIs de flota y ubicación geoespacial.

## Stack Tecnológico
* **Lenguaje:** Python 3.x
* **Librerías:** Pandas, Streamlit, MySQL-Connector
* **Base de Datos:** MySQL / MariaDB (XAMPP)
* **Formato de Datos:** JSON Lines (.jsonl)

## Estructura del Repositorio
- `scripts/`: Automatización de ingesta, ETL y dashboard.
- `data_lake/`: Archivos particionados (Capa Bronze).
- `sql/`: Definición de esquemas de bases de datos relacionales.
- `notebooks/`: Análisis exploratorio de datos (EDA) y validación de sensores.
- `requirements.txt`: Dependencias del proyecto.

## Cómo Ejecutar
1. Clonar el repositorio.
2. Crear la base de datos usando `sql/schema_mineria.sql`.
3. Ejecutar el generador: `python scripts/01_generador_ingesta.py`.
4. Procesar los datos: `python scripts/02_procesamiento_etl.py`.
5. Lanzar el dashboard: `streamlit run scripts/04_dashboard_minero.py`.

---
**Desarrollado por:** Edwin Brayan Benavides Rimarachin  
*Estudiante de Ingeniería de Software con IA | Especialización en Data Engineering para Minería*