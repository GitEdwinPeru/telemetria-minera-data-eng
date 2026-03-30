-- Crear la base de datos si no existe (puedes usar MySQL/XAMPP o PostgreSQL)
CREATE DATABASE IF NOT EXISTS db_mineria_smart;
USE db_mineria_smart;

-- Tabla para almacenar la telemetría procesada (Capa Silver)
CREATE TABLE IF NOT EXISTS telemetria_camiones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp_reporte DATETIME NOT NULL,
    camion_id VARCHAR(20) NOT NULL,
    latitud DECIMAL(10, 8),
    longitud DECIMAL(11, 8),
    temp_motor_c INT,
    rpm INT,
    presion_aceite_psi INT,
    carga_toneladas INT,
    nivel_combustible_pct DECIMAL(5, 2),
    alerta_critica BOOLEAN DEFAULT FALSE -- Para marcar motores calientes (>95C)
);