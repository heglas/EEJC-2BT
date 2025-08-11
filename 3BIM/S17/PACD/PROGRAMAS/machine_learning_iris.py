import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

# Carregando conjunto de dados
iris = datasets.load_iris()

# Separando treino/teste
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, 
                                                    test_size=0.2, 
                                                    random_state=42)

# Criando modelo
model = DecisionTreeClassifier(max_depth=2)

# Treinando modelo
model.fit(X_train, y_train)

# Predizendo
y_pred = model.predict(X_test)

# Acurácia
accuracy = accuracy_score(y_test, y_pred)
print(f"A acurácia do modelo foi de {accuracy:.2f}.")
