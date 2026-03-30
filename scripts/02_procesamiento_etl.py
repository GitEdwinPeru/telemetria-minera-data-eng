import json
import os
import mysql.connector
from datetime import datetime

# Configuración de conexión (Ajusta según tu XAMPP/MySQL)
config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'db_mineria_smart'
}

def procesar_telemetria():
    # 1. EXTRACCIÓN: Buscamos el archivo en el Data Lake
    fecha_hoy = datetime.now().strftime('%Y/%m/%d')
    ruta_archivo = f"data_lake/bronze/{fecha_hoy}/telemetria_raw.jsonl"
    
    if not os.path.exists(ruta_archivo):
        print("❌ No se encontró el archivo de hoy en el Data Lake.")
        return

    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        
        with open(ruta_archivo, 'r') as f:
            for linea in f:
                dato = json.loads(linea)
                
                # 2. TRANSFORMACIÓN: Aplanamos el JSON y creamos la alerta
                es_critico = 1 if dato['motor']['temperatura_c'] > 95 else 0
                
                sql = """INSERT INTO telemetria_camiones 
                         (timestamp_reporte, camion_id, latitud, longitud, temp_motor_c, rpm, 
                          presion_aceite_psi, carga_toneladas, nivel_combustible_pct, alerta_critica)
                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                
                valores = (
                    dato['timestamp'], dato['camion_id'], dato['gps']['lat'], dato['gps']['long'],
                    dato['motor']['temperatura_c'], dato['motor']['rpm'], dato['motor']['presion_aceite_psi'],
                    dato['carga_toneladas'], dato['nivel_combustible_porcentaje'], es_critico
                )
                
                cursor.execute(sql, valores)
        
        conn.commit()
        print(f"✅ Procesamiento exitoso. Datos movidos a la tabla SQL.")
        
        # Opcional: Podrías mover el archivo a 'data_lake/silver' tras procesarlo
        
    except Exception as e:
        print(f"⚠️ Error en el proceso ETL: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    procesar_telemetria()