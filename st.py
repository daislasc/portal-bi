import streamlit as st

st.set_page_config(
    page_title="Portal de Dashboards",
    layout="wide",
    page_icon="ingetek-logo-completo.png"
)

# logo de ingetek completo
st.image("ingetek-logo-completo.png", width=300)
st.title("BI Portal")

# Diccionario: Unidad de negocio -> Dashboards
dashboards = {
    "Finanzas": {
        "Kardex Documentos": {
            "url": "https://lookerstudio.google.com/s/tCRtYVpGMIU",
            "desc": "Control de movimientos de documentos por área",
            "icon": "💰",
            "color": "#2e7d32"
        },
        "Costos de Fabricación": {
            "url": "https://lookerstudio.google.com/s/hvVr9Q0O4LM",
            "desc": "Análisis de costos por planta y línea de producción",
            "icon": "📊",
            "color": "#2e7d32"
        }
    },
    "Facturación": {
        "Embarques y Facturas": {
            "url": "https://lookerstudio.google.com/reporting/f48f9cec-0818-40ce-88d8-40230da24336",
            "desc": "Reporte de facturación consolidado por mes",
            "icon": "🧾",
            "color": "#f57c00"
        }
    },
    "Operación": {
        "Producción": {
            "url": "https://lookerstudio.google.com/s/u80uqadK7oQ",
            "desc": "Toneladas producidas por planta y turno",
            "icon": "🏭",
            "color": "#0288d1"
        }
    }
}

# Función para renderizar tarjetas
def render_card(title, url, desc, icon, color):
    st.markdown(f"""
    <div style="
        border: 1px solid #ddd; 
        border-radius: 12px; 
        padding: 20px; 
        margin: 10px 0; 
        box-shadow: 0 4px 12px rgba(0,0,0,0.15); 
        background-color: #fff;
        min-height: 180px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    ">
        <div style="font-size:32px; margin-bottom:10px;">{icon}</div>
        <h3 style="color:{color}; margin-bottom:8px;">{title}</h3>
        <p style="font-size:14px; color:#555; flex-grow:1;">{desc}</p>
        <a href="{url}" target="_blank" style="
            text-decoration:none; 
            color:white; 
            background-color:{color}; 
            padding:10px 14px; 
            border-radius:6px;
            font-weight:bold;
            text-align:center;
            display:block;
        ">Abrir Dashboard</a>
    </div>
    """, unsafe_allow_html=True)


# 🔹 Crear pestañas por área de negocio
tabs = st.tabs(list(dashboards.keys()))

for (area, reports), tab in zip(dashboards.items(), tabs):
    with tab:
        report_list = list(reports.items())
        cols_per_row = 3  # Ajustable según diseño
        for i in range(0, len(report_list), cols_per_row):
            cols = st.columns(cols_per_row)
            for j, (name, info) in enumerate(report_list[i:i+cols_per_row]):
                with cols[j]:
                    render_card(name, info["url"], info["desc"], info["icon"], info["color"])

