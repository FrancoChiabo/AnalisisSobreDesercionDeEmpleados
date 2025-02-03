#librerias
import streamlit as st
import pandas as pd
import pickle
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from scipy import interpolate

#componentes
from componentes.componente_prediccion import C_prediccion
from componentes.componente_clasificacion import C_clasificacion
from componentes.componente_eda import C_visualizacion

# Configuración de la página
st.set_page_config(page_title="Análisis y Predicción de Empleados", layout="wide")

# Usar HTML para personalizar el tamaño del texto
# Usar HTML para mostrar el logo con borde circular y el texto al lado, con fuente Georgia en 80px
# Usar HTML para mostrar solo el texto "equipoPI" con fuente Georgia en 80px
st.markdown("""
    <style>
        .custom-font {
            font-family: 'Georgia', serif;
            font-size: 100px;  /* Tamaño de fuente 80px */
            color: #FF6347;  /* Cambia el color a tu gusto */
        }
    </style>
    <h1 class="custom-font">equipoPI</h1>
""", unsafe_allow_html=True)


st.markdown("<h1 style='font-size: 50px;'>Análisis del Empleado</h1>", unsafe_allow_html=True)

# Creación de pestañas
tab1, tab2, tab3 = st.tabs(["Visualización EDA", "Modelo de Predicción", "Modelo de Clasificación"])

with open('modelos/modelprediccion.pkl', 'rb') as file1:
    model2 = pickle.load(file1)

with open('modelos/modelclasificacion.pkl', 'rb') as file:
    model1 = pickle.load(file)

df = pd.read_csv("modelos/archivo_combinado.csv")

# Contenido de la pestaña 1: Visualización EDA
with tab1:
    C_visualizacion(df)

# Contenido de la pestaña 2: Modelo de Predicción
with tab2:
    C_prediccion(model2)

# Contenido de la pestaña 3: Modelo de Clasificación
with tab3:
    C_clasificacion(model1)
    