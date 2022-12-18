import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle
from sklearn import svm
import streamlit as st


# Path del modelo preentrenado
MODEL_PATH = 'finalized_model.sav'


#  devuelve la predicción
def model_prediction(x_in, model):

    x = np.asarray(x_in).reshape(1,-1)
    preds=model.predict(x)

    return preds


def main():
    
    model=''

    # Se carga el modelo
    if model=='':
        with open(MODEL_PATH, 'rb') as file:
            model = pickle.load(file)
    
    # Título
    html_temp = """Sistema de predicción de matriculas</h1> </div>"""
    st.markdown(html_temp,unsafe_allow_html=True)

    # Lecctura de datos
    #Datos = st.text_input("Ingrese los valores : AÑO EDAD:")
    anio = st.text_input("AÑO:")
    edad = st.text_input("EDAD:")
    
    
    # El botón predicción se usa para iniciar el procesamiento
    if st.button("Predicción :"): 
        #x_in = list(np.float_((Datos.title().split('\t'))))
        x_in =[np.float_(anio.title()),
                    np.float_(edad.title())]
        predictS = model_prediction(x_in, model)
        st.success('EL AUMENTO DE MATRICULADOS ES DE: {} %'.format(predictS[0]).upper())

if __name__ == '__main__':
    main()