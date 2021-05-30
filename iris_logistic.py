import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Daten einlesen
irisdata = pd.read_csv('iris.csv')

# Daten anpassen
X = irisdata.iloc[:, 0:4]
Y = (irisdata["Class"] == "Iris-virginica").astype(np.int64)  # 1 if Iris-Virginica, else 0

# Model trainieren
model = LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
                   intercept_scaling=1, l1_ratio=None, max_iter=100,
                   n_jobs=None, penalty='l2',
                   random_state=0, solver='liblinear', verbose=0).fit(X, Y)

# Evaluieren
print(model.classes_)

print(classification_report(Y, model.predict(X)))

print('Result of Excercise 2. Master Data Science')
print(model.predict_proba([[4.8, 2.5, 5.3, 2.4]]))
print(model.predict([[4.8, 2.5, 5.3, 2.4]]))

print('Testing with Iris setosa')
print(model.predict(np.array([5.1, 3.5, 1.4, 0.2]).reshape(1, -1)))

print('Testing with 5.7,2.8,4.1,1.3,Iris-versicolor')
print(model.predict(np.array([5.7, 2.8, 4.1, 1.3]).reshape(1, -1)))

print('Testing with 4.9,2.5,4.5,1.7,Iris-virginica')
print(model.predict(np.array([4.9, 2.5, 4.5, 1.7]).reshape(1, -1)))