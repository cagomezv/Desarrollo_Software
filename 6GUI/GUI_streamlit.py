# Importar las librerías
import streamlit as st
import pandas as pd
import plotly.express as px

# Crear DataFrame
data = {
    "ID": [f"{i}" for i in range(10)],
    "Edad": [22, 45, 57, 62, 35, 43, 88, 40, 32, 27],
    "Puntaje": [502, 607, 853, 302, 527, 118, 902, 743, 643, 235]
}
df = pd.DataFrame(data)

# Título de la app
st.title("Streamlit: tutorial introductorio ")

# Barra lateral con opciones
st.sidebar.header("Opciones")
view_mode = st.sidebar.selectbox(
    "Información a mostrar:",
    ["Tabla", "Gráfico Streamlit", "Histograma Plotly"]
)

# Agregar funcionalidad a la barra lateral

# Slider para seleccionar número de filas a mostrar
if view_mode == "Tabla":
    filas_a_mostrar = st.sidebar.slider(
        "Número de filas a mostrar:",
        min_value=1, 
        max_value=10, 
        value=5
    )

# Mostrar tabla
if view_mode == "Tabla":
    st.subheader("Tabla de datos")
    st.write(f"Mostrando las primeras {filas_a_mostrar} filas:")
    st.dataframe(df.head(filas_a_mostrar))

# Mostrar gráfico de streamlit
elif view_mode == "Gráfico Streamlit":
    st.subheader(f"Gráficos {df.columns[1]} y {df.columns[2]}")
    st.line_chart(df.set_index("ID")[["Edad", "Puntaje"]],
                  x_label='ID')

# Mostrar histograma interactivo Plotly
elif view_mode == "Histograma Plotly":

    # Seleccionar columna para el histograma
    columna_histograma = st.sidebar.radio(
        "Seleccione la columna para el histograma:",
        options = df.columns[1:]
    )

    # Título histograma
    st.subheader(f"Histograma Plotly: {columna_histograma}")

    # Graficar histograma
    fig = px.histogram(
        x=df[columna_histograma],
        nbins=5, 
        template="plotly_white"
    )

    fig.update_layout(
        xaxis_title=columna_histograma,
        yaxis_title="Frecuencia",
        bargap=0.1
    )

    st.plotly_chart(fig)
