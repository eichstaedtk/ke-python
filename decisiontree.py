import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from sklearn.tree import export_graphviz
import numpy as np
from sklearn import tree

buycomputer = pd.read_csv('buycomputer.csv', sep=';')

le = preprocessing.OrdinalEncoder()

#buycomputer = buycomputer.apply(le.fit_transform)

Y = buycomputer['Buys_computer'].to_numpy()
X = le.fit_transform(buycomputer[['Age', 'Income', 'Student', 'Credit_rating']])

print(buycomputer)

print(Y)
print(X)

tree_clf = DecisionTreeClassifier(class_weight=None, criterion='entropy', max_depth=5, max_features=None, max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_impurity_split=None,
            min_samples_leaf=1, min_samples_split=2,
            min_weight_fraction_leaf=0.0, random_state=12345, splitter='best')

tree_clf.fit(X, Y)

export_graphviz(
         tree_clf,
         out_file="buycomputer.dot",
         feature_names=['Age', 'Income', 'Student', 'Credit_rating'],
         rounded=True,
         filled=True
 )
