import streamlit as st

st.set_page_config(
    page_title="Portal BI - Ingetek",
    layout="wide",
    page_icon="ingetek-logo.png"
)

# Logo corporativo
st.image("ingetek-logo-completo.png", width=300)
st.title("BI Portal")

# 📘 Leer instructivo desde archivo .md (opcional)
with open("instructivo_dashboards.md", "r", encoding="utf-8") as f:
    instructivo_text = f.read()

# Diccionario principal (cada dashboard tiene: url_dashboard + url_docu + color)
dashboards = {
    "Operación": [
        {
            "title": "Producción",
            "url_dashboard": "https://lookerstudio.google.com/s/u80uqadK7oQ",
            "url_docu": "https://deacero.atlassian.net/wiki/external/NjU0NGE5MWQyZjY0NDcxOTk1Nzk2MGM3YzA2YTk5NmQ",
            "color": "#18515F"
        },
        {
            "title": "Embarques y Facturas",
            "url_dashboard": "https://lookerstudio.google.com/reporting/f48f9cec-0818-40ce-88d8-40230da24336",
            "url_docu": "https://deacero.atlassian.net/wiki/external/YjgyMzA0YTdkNWUyNDgyZWI1NGM5NTA5Zjc0NDMyZjQ",
            "color": "#18515F"
        },
        {
            "title": "Resumen de Órdenes",
            "url_dashboard": "https://lookerstudio.google.com/reporting/b5d47fc5-0c79-43ba-aa0f-774fc41378a1",
            "url_docu": "https://deacero.atlassian.net/wiki/external/NWUyMWViOTgzNDFmNDE5ZGE2YTRhM2RjMmYyMjM1NDE",
            "color": "#18515F"
        },
        {
            "title": "Inventario",
            "url_dashboard": "https://lookerstudio.google.com/u/0/reporting/6ea32ee4-1970-4116-99d0-c6a8fe2e9efa/page/p_hvqg5pwhwd/edit",
            "url_docu": "https://deacero.atlassian.net/wiki/external/M2Q1ZjczYWRlMDkzNDU3MWJhNWRjYjJjM2Y5ZTRmMTU",
            "color": "#18515F"
        }
    ],
    "Contabilidad y Finanzas": [
        {
            "title": "Costos de Fabricación",
            "url_dashboard": "https://lookerstudio.google.com/s/hvVr9Q0O4LM",
            "url_docu": "https://deacero.atlassian.net/wiki/external/YjgyMzA0YTdkNWUyNDgyZWI1NGM5NTA5Zjc0NDMyZjQ",
            "color": "#18515F"
        }
    ],
    "Back-Office": [
        {
            "title": "Kardex Documentos",
            "url_dashboard": "https://lookerstudio.google.com/s/tCRtYVpGMIU",
            "url_docu": "https://deacero.atlassian.net/wiki/external/YjgyMzA0YTdkNWUyNDgyZWI1NGM5NTA5Zjc0NDMyZjQ",
            "color": "#18515F"
        }
    ],
    "Comercial": [
        {
            "title": "Proyectos Contratados",
            "url_dashboard": "https://lookerstudio.google.com/reporting/5ada6ad5-d915-469e-b9e3-c5ad7816ae08",
            "url_docu": "https://deacero.atlassian.net/wiki/external/YjE5NWU1ZDYwMjY5NDc4N2E3NjM3YTM1Njc4NjA3NjY",
            "color": "#18515F"
        },
        {
            "title": "Deuda Comercial",
            "url_dashboard": "https://lookerstudio.google.com/reporting/746dd37b-1c5c-44a2-87f5-8a854571f2f3/page/gdQZF",
            "url_docu": "https://deacero.atlassian.net/wiki/external/YjE5NWU1ZDYwMjY5NDc4N2E3NjM3YTM1Njc4NjA3NjY",
            "color": "#18515F"
        }
    ],
    "Looker Studio Docs": [
        {
            "title": "Dashboard Ejemplo",
            "url_dashboard": "https://lookerstudio.google.com/s/u80uqadK7oQ",
            "url_docu": "https://deacero.atlassian.net/wiki/spaces/~63c73454176040ff3bd1be39/pages/1757839401/Instructivo+para+Crear+y+Editar+Dasboards+en+Looker+Studio",
            "color": "#18515F"
        }
    ]
}

# Función para renderizar tarjetas
def render_card(title, url_dashboard, url_docu, color):
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
        <p style="font-size:14px; color:#18515F; font-weight:bold;">
            <a href="{url_docu}" target="_blank" style="color:{color}; text-decoration:underline;">
                Documentación y Autoservicio
            </a>
        </p>
        <a href="{url_dashboard}" target="_blank" style="
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

# 🔹 Barra lateral (solo secciones)
st.sidebar.title("Menú de Navegación")
selected_section = st.sidebar.radio("Secciones:", list(dashboards.keys()))

# 🔹 Render dinámico
st.header(selected_section)

content = dashboards[selected_section]
if not content:
    st.info("No hay dashboards disponibles en esta sección.")
else:
    cols_per_row = 3
    for i in range(0, len(content), cols_per_row):
        cols = st.columns(cols_per_row)
        for j, info in enumerate(content[i:i+cols_per_row]):
            with cols[j]:
                render_card(info["title"], info["url_dashboard"], info["url_docu"], info["color"])
