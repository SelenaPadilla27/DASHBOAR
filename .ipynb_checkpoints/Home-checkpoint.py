import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import geopandas as gpd
import numpy as np
# Icono y configuracion basico del tablero digital
#__________________________________________________________________________________________________________________________________________________
st.set_page_config(layout="wide",
                   page_icon="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png",
                   page_title="Web app")
# --------------------------------------------------------------------------------------------------------------------------------------------------
# Cargue y guardado en la cache de los datos provenientes de los dataframe usados 
@st.cache(allow_output_mutation=True)
def cargar_datos(filename: str):
    return pd.read_csv(filename)
#Asignacion a la variable que usara en todo el tablero
datos = cargar_datos("consolidado_2010_2021.csv")

#@st.cache
def cargar_mapa(file: str):
    return pd.read_json(file)
map_depts = cargar_mapa("MunicipiosVeredas.json")

#@st.cache
def cargar_departamentos_colombia(fileN:str):
    return pd.read_csv(fileN,sep=";")
depts = cargar_departamentos_colombia("Departamentos.csv")
#---------------------------------------------------------------------------------------------------------------------------------------------------
#Elementos que estaran en el sidebar lateral
st.sidebar.image("logo.png")
 
#---------------------------------------------------------------------------------------------------------------------------------------------------
#Cabezera del tablero digital
st.header("ESTADÍSTICAS COLOMBIANA SOBRE MATRICULAS EN LOS COLEGIOS DEL TERRITORIO NACIONAL POR MUNICIPIOS DEL DEPARTAMENTO DE CORDOBA CÓRDOBA.")

#---------------------------------------------------------------------------------------------------------------------------------------------------

# Cuerpo general de la primera pagina del tablero
#Funcion que crea el primer grafico de barras, esta es guardada en la cache para una mejor velocidad de carga del tablero digital
#@st.cache(allow_output_mutation=True)
st.header("CANTIDAD DE ESTUDIANTES MATRICULADOS POR AÑO DESDE EL 2010 HASTA EL 2021.")
def grafico_bar(datos_bar):
    annios = datos_bar["AÑO"]
    datos_bar = datos_bar.set_index("AÑO")
    fig = px.line(
        datos_bar.groupby([datos_bar.index])["TOTAL MATRICULA"]
        .count(),
        y="TOTAL MATRICULA",
        text='TOTAL MATRICULA',
    )
    return fig


varfig = grafico_bar(datos)
st.plotly_chart(
    varfig,
    use_container_width=True
)
#@st.cache(allow_output_mutation=True)
st.header("CANTIDAD DE ESTUDIANTES MATRICULADOS POR MUNICIPIOS.")
def grafico_bar2(data_grafico):
    cantidad_matriculas_zonas = data_grafico.groupby(["MUNICIPIO"])[["TOTAL MATRICULA"]].count()
    cantidad = np.sort(cantidad_matriculas_zonas["TOTAL MATRICULA"].unique())
    municipios = data_grafico["MUNICIPIO"].unique()
    fig = px.bar(
        data_grafico.groupby(["MUNICIPIO"])[["TOTAL MATRICULA"]].count()
        .sort_values(by="TOTAL MATRICULA"),
        color = "TOTAL MATRICULA",
        #color_continuous_scale=px.colors.sequential.bluered,
        color_continuous_scale = "bluyl",
        y = "TOTAL MATRICULA"
    )
    return fig

varfig2 = grafico_bar2(datos)
st.plotly_chart(
    varfig2,
    use_container_width=True
)

#---------------------------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------------
