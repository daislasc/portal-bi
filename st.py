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

# Diccionario principal
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
            },
            "Inventario": {
                "url": "https://lookerstudio.google.com/u/0/reporting/6ea32ee4-1970-4116-99d0-c6a8fe2e9efa/page/p_ee36dyg2vd/edit",
                "desc": "Inventario de Productos en Almacenes de INGETEK",
                "color": "#18515F"
            }
        },
        # 🔹 Estructura nueva: cada dashboard tiene Plantilla + Documentación
        "documentacion": {
            "Embarques y Facturas": {
                "plantilla": {
                    "url": "https://lookerstudio.google.com/u/0/reporting/96bd7f9a-ad9c-4b02-a866-28dab9b0816c/page/p_ee36dyg2vd/preview",
                    "desc": "Personaliza tu propio reporte de Embarques",
                },
                "documentacion": {
                    "url": "https://deacero.atlassian.net/wiki/external/YjgyMzA0YTdkNWUyNDgyZWI1NGM5NTA5Zjc0NDMyZjQ",
                    "desc": "Descripción general de los campos a utilizar en el Dashboard.",
                },
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
    },

    "Looker Studio":{
        "dashboards":{
            "Dashboard Ejemplo":{
                "url": "https://lookerstudio.google.com/s/u80uqadK7oQ",
                "desc": "Ejemplo",
                "color": "#18515F"
            }
        },
        "documentacion": {
            "Looker Studio": {
                "plantilla": {
                    "url": "https://lookerstudio.google.com/navigation/templates",
                    "desc": "Templates Generales Looker Studio",
                },
                "documentacion": {
                    "url": "https://deacero.atlassian.net/wiki/spaces/~63c73454176040ff3bd1be39/pages/1757839401/Instructivo+para+Crear+y+Editar+Dasboards+en+Looker+Studio",
                    "desc": "Instructivo para Crear y Editar Dashboards en Looker Studio",
                },
                "color": "#18515F"
            }
        }
    }
}


# Función para renderizar tarjetas normales
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

# 🔹 Barra lateral
st.sidebar.title("Menú de Navegación")

selected_section = st.sidebar.radio("Secciones:", list(dashboards.keys()))
subsection = st.sidebar.radio("Subsección:", ["Dashboards", "Documentación y Autoservicio"])

# 🔹 Render dinámico
st.header(f"{selected_section} - {subsection}")

if subsection == "Dashboards":
    content = dashboards[selected_section]["dashboards"]
    if not content:
        st.info("No hay dashboards disponibles en esta sección.")
    else:
        items = list(content.items())
        cols_per_row = 3
        for i in range(0, len(items), cols_per_row):
            cols = st.columns(cols_per_row)
            for j, (name, info) in enumerate(items[i:i+cols_per_row]):
                with cols[j]:
                    render_card(name, info["url"], info["desc"], info["color"])

else:  # Documentación y Autoservicio
    content = dashboards[selected_section]["documentacion"]
    if not content:
        st.info("No hay documentación disponible en esta sección.")
    else:
        for dashboard_name, data in content.items():
            color = data.get("color", "#18515F")
            with st.expander(f"Autoservicio de {dashboard_name}", expanded=False):
                st.markdown(f"""
                <p><b>Plantilla:</b> <a href="{data['plantilla']['url']}" target="_blank">{data['plantilla']['desc']}</a></p>
                <p><b>Documentación:</b> <a href="{data['documentacion']['url']}" target="_blank">{data['documentacion']['desc']}</a></p>
                """, unsafe_allow_html=True)
