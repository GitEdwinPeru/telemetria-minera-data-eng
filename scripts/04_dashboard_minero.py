import streamlit as st
import pandas as pd
import mysql.connector
from datetime import datetime

# Configuración de página
st.set_page_config(page_title="Mining Fleet Monitor", layout="wide")

def get_data():
    conn = mysql.connector.connect(
        host="127.0.0.1", user="root", password="", database="db_mineria_smart"
    )
    query = "SELECT * FROM telemetria_camiones ORDER BY timestamp_reporte DESC LIMIT 100"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

st.title("🚜 Monitor de Telemetría - Flota Minera")
st.write(f"Actualizado: {datetime.now().strftime('%H:%M:%S')}")

# Obtener datos
df = get_data()

if not df.empty:
    # --- KPIs PRINCIPALES ---
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Reportes", len(df))
    with col2:
        alertas = df[df['alerta_critica'] == 1].shape[0]
        st.metric("Alertas Críticas", alertas, delta=f"{alertas} incidentes", delta_color="inverse")
    with col3:
        prom_temp = round(df['temp_motor_c'].mean(), 1)
        st.metric("Temp. Promedio Motor", f"{prom_temp}°C")

    # --- GRÁFICOS ---
    st.subheader("Evolución de Temperatura por Camión")
    st.line_chart(df.pivot(columns='camion_id', values='temp_motor_c'))

    # --- MAPA DE CALOR (Simulado con los puntos GPS) ---
    st.subheader("Ubicación de Unidades en Tajo")
    # Streamlit necesita columnas llamadas 'lat' y 'lon'
    map_df = df[['latitud', 'longitud']].rename(columns={'latitud': 'lat', 'longitud': 'lon'})
    st.map(map_df)

    # --- TABLA DE DATOS ---
    st.subheader("Últimos Registros Procesados")
    st.dataframe(df)
else:
    st.warning("No hay datos en la base de datos. Ejecuta el script ETL primero.")

# Botón para refrescar
if st.button('Actualizar Datos'):
    st.rerun()