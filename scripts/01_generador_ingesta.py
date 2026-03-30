import os
import json
import time
import random
from datetime import datetime

# Función para simular el camión (Origen)
def generar_lectura_camion(id_camion):
    return {
        "timestamp": datetime.now().isoformat(),
        "camion_id": id_camion,
        "gps": {
            "lat": round(random.uniform(-15.120, -15.130), 6),
            "long": round(random.uniform(-70.580, -70.590), 6)
        },
        "motor": {
            "temperatura_c": random.randint(70, 110),
            "rpm": random.randint(1500, 2200),
            "presion_aceite_psi": random.randint(40, 70)
        },
        "carga_toneladas": random.randint(300, 400),
        "nivel_combustible_porcentaje": round(random.uniform(10, 100), 2)
    }

# Función de Ingesta (Almacenamiento en Data Lake)
def guardar_en_datalake(dato):
    # Ruta relativa para que funcione desde la carpeta principal
    fecha_hoy = datetime.now()
    path = f"data_lake/bronze/{fecha_hoy.strftime('%Y/%m/%d')}"
    
    if not os.path.exists(path):
        os.makedirs(path)
    
    archivo_nombre = f"{path}/telemetria_raw.jsonl"
    with open(archivo_nombre, "a") as f:
        f.write(json.dumps(dato) + "\n")

# Ejecución principal
if __name__ == "__main__":
    print("🛰️  Iniciando generación de datos mineros...")
    print("📂 Guardando en: data_lake/bronze/...")
    try:
        while True:
            lectura = generar_lectura_camion("CAT-797-001")
            guardar_en_datalake(lectura)
            print(f"✅ Lectura guardada: {lectura['timestamp']} | Temp: {lectura['motor']['temperatura_c']}°C")
            time.sleep(2) 
    except KeyboardInterrupt:
        print("\n⏹️  Proceso detenido.")