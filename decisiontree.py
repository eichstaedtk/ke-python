import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
import category_encoders as ce

buycomputer = pd.read_csv('buycomputer.csv', sep=';')

le = ce.OrdinalEncoder(cols=['Age', 'Income', 'Student', 'Credit_rating'])

Y = buycomputer['Buys_computer'].to_numpy()
X = le.fit_transform(buycomputer[['Age', 'Income', 'Student', 'Credit_rating']]).to_numpy()

print(buycomputer)

print(Y)
print(X)

tree_clf = DecisionTreeClassifier(class_weight=None, criterion='entropy', max_depth=10, splitter='best')

tree_clf.fit(X, Y)

export_graphviz(
         tree_clf,
         out_file="buycomputer.dot",
         feature_names=['Age', 'Income', 'Student', 'Credit_rating'],
             class_names=['Buy', 'Not_Buy'],
         rounded=True,
         filled=True,
 )
