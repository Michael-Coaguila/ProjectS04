import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# Título y descripción para el usuario
st.title("Análisis de datos de vehículos")
st.write("Seleccione las visualizaciones que desea generar a partir del conjunto de datos de anuncios de vehículos:")

# Elementos de la interfaz de usuario
build_histogram = st.checkbox('Mostrar Histograma de Odómetro')
build_scatter = st.checkbox('Mostrar Gráfico de Dispersión de Odómetro vs Precio')

# Si el usuario desea ver el histograma
if build_histogram:
    st.subheader("Histograma de Odómetro")
    fig_hist = px.histogram(car_data, x="odometer", title="Distribución de Odómetro")
    st.plotly_chart(fig_hist, use_container_width=True)

# Si el usuario desea ver el gráfico de dispersión
if build_scatter:
    st.subheader("Gráfico de Dispersión: Odómetro vs Precio")
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Odómetro vs Precio")
    st.plotly_chart(fig_scatter, use_container_width=True)