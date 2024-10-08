# -*- coding: utf-8 -*-
"""rendimentoescolar.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_VQlDNHyVOwDLeqtpxbUqb0Ipo7L1bBl

Imports necessários
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

"""Lendo a base de dados"""

data = pd.read_csv('PlanilhaDadosATTFormulas.csv')
data.head()

"""Separando x e y"""

Xvariaveis = data.drop(['Nome (codificado)', 'Data de Nascimento', '9º MAT'], axis=1)
y = data['9º MAT']
Xvariaveis.dtypes

"""Separando em conjuntos"""

X_train, X_test, y_train, y_test = train_test_split(Xvariaveis, y, test_size=0.75, random_state=42)

"""Criando Modelo (utilizando Regressor ao invés do Classifier devido ao Regressor conseguir prever valores não classificavéis, como números de pontos flutuantes distintos)"""

model = RandomForestRegressor(n_estimators=100, random_state=42)

"""Treinando Modelo"""

model.fit(X_train, y_train)

"""Prevendo com valores de teste"""

y_pred = model.predict(X_test)

"""Avaliando eficácia do modelo

*   O MSE é uma métrica comum para avaliar o desempenho de modelos de regressão. Ele calcula a média dos quadrados das diferenças entre os valores previstos pelo modelo e os valores reais observados no conjunto de teste.
*   Um valor de MSE menor indica que o modelo, em média, fez previsões mais próximas dos valores reais.
"""

mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

"""Armazenando importância das variáveis"""

importances = model.feature_importances_
print(importances)

"""Renderizando importância das variáveis"""

plt.figure(figsize=(45, 6))
plt.bar(Xvariaveis.columns, importances)
plt.xlabel("Variáveis")
plt.ylabel("Importância")
plt.title("Importância de Recursos (Random Forest)")
fig = plt.gcf()
plt.show()

import os
nome_arquivo = "grafico.png"
diretorio = os.path.join(os.getcwd())
fig.savefig(os.path.join(diretorio, nome_arquivo))