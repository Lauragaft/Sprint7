import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="EDA Sprint 7", layout="wide")
st.header("Análisis de anuncios de vehículos")

@st.cache_data
def load_data():
    return pd.read_csv("vehicles_us.csv")

car_data = load_data()

build_hist = st.checkbox("Construir histograma")
build_scatter = st.checkbox("Construir gráfico de dispersión")

if build_hist:
    st.write("Creación de un histograma para la columna **odometer**")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:
    st.write("Creación de un gráfico de dispersión **price vs odometer**")
    fig2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)

