import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import geopandas as gpd
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

#@st.cache(allow_output_mutation=True)
def cargar_mapa(file: str):
    return pd.read_json(file)
map_depts = cargar_mapa("MunicipiosVeredas.json")

#@st.cache(allow_output_mutation=True)
def cargar_departamentos_colombia(fileN:str):
    return pd.read_csv(fileN,sep=";")
depts = cargar_departamentos_colombia("Departamentos.csv")

st.sidebar.image("logo.png")



geo_map = gpd.GeoDataFrame.from_features(map_depts["features"]).merge(depts, on="MPIO_CNMBR")
geo_map.drop([0,2], axis=0, inplace=True)
geo_map = geo_map.set_index("MPIO_CNMBR")
    
#@st.cache(allow_output_mutation=True)
def Mapa_interactivo(gep_mapa):
    fig = px.choropleth_mapbox(geo_map,
                           geojson=geo_map.geometry,
                           locations=geo_map.index,
                           color='CANT_MATRICULADOS',
                           color_continuous_scale='bluyl',
                           mapbox_style="carto-positron",
                           zoom=6, center = {'lat': 8.74798, 'lon': -75.88143},
                           opacity=0.5,
                          )
    return fig
st.write("# MAPA INTERACTIVO, CANTIDAD DE MATRICULADOS POR MUNICIPIOS EN CÓRDOBA")
st.write("### La importacia de recolectar información de las matrículas estadísticas en Colombia brinda a la nación la planeación del servicio educativo, distribuir recursos, tomar decisiones, generar estadísticas y construir indicadores que apoyen la formulación de políticas educativas.")
st.plotly_chart(Mapa_interactivo(geo_map), use_container_width = True)