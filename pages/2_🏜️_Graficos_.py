import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import geopandas as gpd



st.set_page_config(layout="wide",
                   page_icon="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png",
                   page_title="Web app")
@st.cache(allow_output_mutation=True)
def cargar_datos(filename: str):
    return pd.read_csv(filename)
#Asignacion a la variable que usara en todo el tablero
datos = cargar_datos("consolidado_2010_2021.csv")


st.sidebar.image("logo.png")



col1,col2 = st.columns(2)

with col1:
    op=[x for x in datos.columns if datos[x].dtype != "int64" and datos[x].nunique()<10 and datos[x].nunique()>1 and x != "SECRETARIA" and x != "CARACTER" and x != "ESPECIALIDAD"]
    op_pie = st.selectbox(label="LISTA DE OPCIONES PARA GRAFICO PIE",options = op)

options_dict = {
    
}
#Grafico pie tambien se guardan en la cache
#@st.cache(allow_output_mutation=True)
def pie_Figure(df_pie, x):
    sizes = df_pie[x].value_counts().tolist()
    labels = df_pie[x].dropna().unique()
    fig = px.pie(datos,
             values=sizes,
             names=labels,
             title='Grafico pie para opcines no numericas',
             #color = labels,
             color_discrete_sequence=px.colors.qualitative.Set3
            )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig
st.plotly_chart(pie_Figure(datos, op_pie))

#Grafico funnel para Masculinos
def grafico_funnel_masculinos(data_funnel,seleccion):
    data_funnel = data_funnel[data_funnel.GENERO == "M"]
    x1 = data_funnel[seleccion].value_counts().tolist()
    y1 = data_funnel[seleccion].unique()
    fig = px.funnel(data_funnel, x=x1, y=y1)
    return fig
#Grafico funnel para Femeninos
def grafico_funnel_femeninas(data_funnel,seleccion):
    data_funnel = data_funnel[data_funnel.GENERO == "F"]
    x1 = data_funnel[seleccion].value_counts().tolist()
    y1 = data_funnel[seleccion].unique()
    fig = px.funnel(data_funnel, x=x1, y=y1,color_discrete_sequence = ['lightcoral'], opacity = 1)
    return fig
col4, col5 = st.columns(2)
with col4:
    st.markdown("Opcion "+op_pie+" desglosada por sexo femenino")
    st.plotly_chart(grafico_funnel_femeninas(datos,op_pie), use_container_width=True)
with col5:
    st.markdown("Opcion "+op_pie+" Desglosada por sexo masculino")
    st.plotly_chart(grafico_funnel_masculinos(datos,op_pie), use_container_width=True)
