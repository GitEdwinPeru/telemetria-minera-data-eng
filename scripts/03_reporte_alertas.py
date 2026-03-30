import mysql.connector
from datetime import datetime

config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'db_mineria_smart'
}

def generar_reporte_mantenimiento():
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        
        # Consulta de agregación: Contamos cuántas alertas tiene cada camión
        query = """
            SELECT camion_id, COUNT(*) as total_alertas, MAX(temp_motor_c) as max_temp
            FROM telemetria_camiones
            WHERE alerta_critica = 1
            GROUP BY camion_id
            HAVING total_alertas > 0
            ORDER BY max_temp DESC;
        """
        
        cursor.execute(query)
        resultados = cursor.fetchall()
        
        print(f"\n--- ⚠️ REPORTE DE ALERTAS DE MANTENIMIENTO ({datetime.now().strftime('%Y-%m-%d')}) ---")
        if not resultados:
            print("✅ No hay alertas críticas registradas. Operación segura.")
        else:
            print(f"{'CAMIÓN ID':<15} | {'ALERTAS':<10} | {'MÁX TEMP (°C)':<15}")
            print("-" * 45)
            for fila in resultados:
                print(f"{fila[0]:<15} | {fila[1]:<10} | {fila[2]:<15}")
                
    except Exception as e:
        print(f"❌ Error al generar reporte: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    generar_reporte_mantenimiento()