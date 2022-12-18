import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sn

data = pd.read_csv("consolidado_2010_2021.csv")
data.shape

data.head()

#validacion de datos nulos
data.isnull().sum()

#correlaciones
sn.heatmap(data.corr(), annot=True)
plt.show

#MODELO 1

# librerias regresion lineal
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
#seleccion de caracteristicas
X = data[['ANNO_INF','EDAD']] #variable predictora
Y = data[['TOTAL_MATRICULA']] #variable respuesta
# train & set sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3,random_state=1)
#instanciar modelo
model1 = LinearRegression()
#ajuste del modelo
model1.fit(X_train, Y_train)
#estimación de parametros
model1.intercept_.round(2)
# predicciones con el X_test
y_test_predicted1 = model1.predict(X_test)

#EVALUACION MODELO 1

# MSE - Mean Squared Error
from sklearn.metrics import mean_squared_error

print(mean_squared_error(Y_test, y_test_predicted1))

# R - squared
print(model1.score(X_test, Y_test))

#MODELO 2

# librerias regresion lineal
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
#seleccion de caracteristicas
X = data[['ANNO_INF']] #variable predictora
Y = data[['TOTAL_MATRICULA']] #variable respuesta
# train & set sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3,random_state=1)
#instanciar modelo
model2 = LinearRegression()
#ajuste del modelo
model2.fit(X_train, Y_train)
#estimación de parametros
model2.intercept_.round(2)
# predicciones con el X_test
y_test_predicted2 = model2.predict(X_test)

#EVALUACION MODELO 2

# MSE - Mean Squared Error
from sklearn.metrics import mean_squared_error

print(mean_squared_error(Y_test, y_test_predicted2))

# R - squared
print(model2.score(X_test, Y_test))

import pickle
# guadar modelo
filename = 'finalized_model.sav'
pickle.dump(model1, open(filename, 'wb'))