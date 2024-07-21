# -*- coding: utf-8 -*-
"""Teste.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13dVApPqvI7oDozuitXQWRu1juLyGsTlP

Bibliotecas mais importantes
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

"""Carregando a base de dados"""

data = pd.read_csv('student-mat-v3.csv')
data.head()

"""Separando variáveis de treino e de resultado"""

X = data.drop('FINAL', axis=1)
y = data['FINAL']
X.head()

"""Separando em conjuntos"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.75, random_state=42)

"""Criando modelo de treinamento"""

model = RandomForestClassifier(n_estimators=100, random_state=42)

"""Treinando Modelo"""

model.fit(X_train, y_train)

"""Fazendo previsões"""

y_pred = model.predict(X_test)

"""Avaliando Eficiência do modelo"""

accuracy = accuracy_score(y_test, y_pred)
print('Acurácia:', accuracy)