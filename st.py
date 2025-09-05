import streamlit as st

st.set_page_config(
    page_title="Portal BI - Ingetek",
    layout="wide",
    page_icon="ingetek-logo.png"
)

# logo de ingetek completo
st.image("ingetek-logo-completo.png", width=300)
st.title("BI Portal")

# 📘 Leer instructivo desde archivo .md
with open("instructivo_dashboards.md", "r", encoding="utf-8") as f:
    instructivo_text = f.read()

# Diccionario: Unidad de negocio -> Dashboards
dashboards = {
    "Operación": {
        "Processing Tag": {
            "url": "https://lookerstudio.google.com/s/u80uqadK7oQ",
            "desc": "Detalle de Producción en INGETEK",
            "icon": "🏭",
            "color": "#18515F"
        },
        "Shipping Tickets": {
                    "url": "https://lookerstudio.google.com/reporting/f48f9cec-0818-40ce-88d8-40230da24336",
                    "desc": "Detalle de Embarques y Facturas en INGETEK",
                    "icon": "🚚",
                    "color": "#18515F"
        },
        "Control Code (Order Summary)": {
                    "url": "https://lookerstudio.google.com/reporting/b5d47fc5-0c79-43ba-aa0f-774fc41378a1",
                    "desc": "Resúmenes de Órdenes y Control Code en INGETEK",
                    "icon": "🧾",
                    "color": "#18515F"
        }
    },

    "Contabilidad y Finanzas": {
        "Costos de Fabricación": {
            "url": "https://lookerstudio.google.com/s/hvVr9Q0O4LM",
            "desc": "Análisis contable por planta y agrupadores de gestión en INGETEK",
            "icon": "📊",
            "color": "#18515F"
            }
    },

    "Back-Office":{
        "Kardex Documentos": {
            "url": "https://lookerstudio.google.com/s/tCRtYVpGMIU",
            "desc": "Control de movimientos de documentos por área en INGETEK",
            "icon": "📑",
            "color": "#18515F"
        }
    },

    "Documentación y Autoservicio": {
        "Plantilla - Shipping Tickets": {
            "url": "https://lookerstudio.google.com/reporting/5eb49aa4-aecb-4af6-8548-1fc86a1416eb/preview",
            "desc": "Personaliza tu propio reporte de Embarques",
            "icon": "🎨",
            "color": "#18515F"
        },
        "Guía Looker Studio": {
            "url": "#",  # <- Indicamos que es un instructivo interno
            "desc": "Aprende buenas prácticas para crear y editar dashboards.",
            "icon": "📘",
            "color": "#18515F"
        }
    }
}

# Función para renderizar tarjetas
def render_card(title, url, desc, icon, color):
    if url == "#":
        # Caso especial: mostrar instructivo dentro de la app
        with st.expander(f"{icon} {title}"):
            st.markdown(instructivo_text, unsafe_allow_html=True)
    else:
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

