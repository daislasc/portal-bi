import streamlit as st

st.set_page_config(
    page_title="Portal BI - Ingetek",
    layout="wide",
    page_icon="ingetek-logo.png"
)

# Logo corporativo
st.image("ingetek-logo-completo.png", width=300)
st.title("BI Portal")

# 📘 Leer instructivo desde archivo .md
with open("instructivo_dashboards.md", "r", encoding="utf-8") as f:
    instructivo_text = f.read()

# Diccionario principal SIN íconos
dashboards = {
    "Operación": {
        "dashboards": {
            "Producción": {
                "url": "https://lookerstudio.google.com/s/u80uqadK7oQ",
                "desc": "Detalle de Producción en INGETEK",
                "color": "#18515F"
            },
            "Embarques y Facturas": {
                "url": "https://lookerstudio.google.com/reporting/f48f9cec-0818-40ce-88d8-40230da24336",
                "desc": "Detalle de Embarques y Facturas en INGETEK",
                "color": "#18515F"
            },
            "Resumen de Órdenes": {
                "url": "https://lookerstudio.google.com/reporting/b5d47fc5-0c79-43ba-aa0f-774fc41378a1",
                "desc": "Resúmenes de Órdenes y Control Code en INGETEK",
                "color": "#18515F"
            }
        },
        "documentacion": {
            "Plantilla - Embarques y Facturas": {
                "url": "https://lookerstudio.google.com/reporting/f1120983-20f8-4f93-b630-6a3b04f7e61c/preview",
                "desc": "Personaliza tu propio reporte de Embarques",
                "color": "#18515F"
            },
            "Guía Looker Studio": {
                "url": "https://deacero.atlassian.net/wiki/spaces/~63c73454176040ff3bd1be39/pages/1757839401/Instructivo+para+Crear+y+Editar+Dasboards+en+Looker+Studio",
                "desc": "Aprende buenas prácticas para crear y editar dashboards.",
                "color": "#18515F"
            }
        }
    },

    "Contabilidad y Finanzas": {
        "dashboards": {
            "Costos de Fabricación": {
                "url": "https://lookerstudio.google.com/s/hvVr9Q0O4LM",
                "desc": "Análisis contable por planta y agrupadores de gestión en INGETEK",
                "color": "#18515F"
            }
        },
        "documentacion": {}
    },

    "Back-Office": {
        "dashboards": {
            "Kardex Documentos": {
                "url": "https://lookerstudio.google.com/s/tCRtYVpGMIU",
                "desc": "Control de movimientos de documentos por área en INGETEK",
                "color": "#18515F"
            }
        },
        "documentacion": {}
    }
}

# Función para renderizar tarjetas SIN iconos
def render_card(title, url, desc, color):
    st.markdown(f"""
    <div style="
        border: 1px solid #ddd; 
        border-radius: 12px; 
        padding: 20px; 
        margin: 10px 0; 
        box-shadow: 0 4px 12px rgba(0,0,0,0.15); 
        background-color: #fff;
        min-height: 160px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    ">
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
        ">Abrir</a>
    </div>
    """, unsafe_allow_html=True)

# 🔹 Barra lateral de navegación
st.sidebar.title("Menú de Navegación")

selected_section = st.sidebar.radio("Secciones:", list(dashboards.keys()))
subsection = st.sidebar.radio(
    "Subsección:",
    ["Dashboards", "Documentación y Autoservicio"]
)

# 🔹 Renderizado dinámico según selección
st.header(f"{selected_section} - {subsection}")

content = (
    dashboards[selected_section]["dashboards"]
    if subsection == "Dashboards"
    else dashboards[selected_section]["documentacion"]
)

if not content:
    st.info("No hay contenido disponible en esta subsección.")
else:
    items = list(content.items())
    cols_per_row = 3
    for i in range(0, len(items), cols_per_row):
        cols = st.columns(cols_per_row)
        for j, (name, info) in enumerate(items[i:i+cols_per_row]):
            with cols[j]:
                render_card(name, info["url"], info["desc"], info["color"])
